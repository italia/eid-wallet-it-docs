#!/bin/bash

# =============================================================================
# RST Translation Script
# =============================================================================
# Translates RST files from English to Italian using an AI translation API
# =============================================================================

if [ $# -eq 0 ]; then
  echo "Usage: $0 <file1.rst> <file2.rst> ..."
  exit 1
fi

# =============================================================================
# Environment Variables Validation
# =============================================================================

required_vars=("GEMINI_API_KEY" "GEMINI_SYSTEM_PROMPT" "GEMINI_USER_PROMPT"
               "GEMINI_GLOSSARY" "TEMPERATURE" "TOP_P" "TOP_K"
               "MODEL" "OUTPUT_DIR")

for var in "${required_vars[@]}"; do
  if [ -z "${!var}" ]; then
    echo "Error: $var environment variable not set."
    exit 1
  fi
done

# =============================================================================
# Dependencies Check
# =============================================================================

if ! command -v jq &> /dev/null; then
  echo "Error: jq is not installed. Install it using 'apt-get install jq'."
  exit 1
fi

# =============================================================================
# Setup and Configuration
# =============================================================================

mkdir -p "${OUTPUT_DIR}"/

# API limits chunking configuration
MAX_CHUNK_SIZE=8000         # Maximum chunk size expressed in number of characters. A single token is approximately made of 3 characters and in avarage the expansion of translating english text in italian is 50%, so 8000 characters may be expandend in 12000 characters, resulting in approximately 4000 tokens, way under the current 8192 output token limit.
MAX_OUTPUT_TOKENS=8192      # Output token limit

# Retry configuration
MAX_RETRIES=3
BASE_RETRY_DELAY=2
RATE_LIMIT_DELAY=60
SERVICE_UNAVAILABLE_DELAY=60

# Truncation marker for incomplete translations
TRUNCATION_MARKER="

.. warning::
   ⚠️⚠️⚠️ **TRADUZIONE INCOMPLETA** ⚠️⚠️⚠️
   - Il contenuto è stato troncato per limiti di token. Parte del testo originale non è stata tradotta.

"
# Block marker for blocked translations
BLOCK_MARKER="

.. warning::
   🚫🚫🚫 **CONTENUTO BLOCCATO** 🚫🚫🚫
   - La traduzione di questo segmento è stata bloccata dai filtri di sicurezza del modello.
    
"

# =============================================================================
# Utility Functions
# =============================================================================

# logging
log_error() {
  echo "❌ ERROR: $*" >&2
}

log_warning() {
  echo "⚠️ WARNING: $*" >&2
}

log_info() {
  echo "ℹ️ INFO: $*"
}

# Exponential backoff with jitter
calculate_retry_delay() {
  local attempt=$1
  local base_delay=$2
  local delay=$((base_delay * (2 ** (attempt - 1))))
  # Add jitter (random 0-25% of delay)
  local jitter=$((delay / 4))
  local random_jitter=$((RANDOM % (jitter > 0 ? jitter : 1)))
  echo $((delay + random_jitter))
}

# =============================================================================
# Line-Aware Chunking Function
# =============================================================================

CHUNKS=()
create_chunks() {
  local content="$1"
  local file_size=${#content}
  local chunks=()

  echo "📄 File size: $file_size characters"

  if [ $file_size -le $MAX_CHUNK_SIZE ]; then
    echo "📄 File size within chunk limit, processing as single piece"
    chunks=("$content")
  else
    echo "🔀 File exceeds chunk limit, splitting into chunks..."

    local pos=0
    local chunk_num=1

    while [ $pos -lt $file_size ]; do
      local remaining=$((file_size - pos))

      # If remaining content is smaller than chunk size, take it all
      if [ $remaining -le $MAX_CHUNK_SIZE ]; then
        local final_chunk="${content:$pos}"
        chunks+=("$final_chunk")
        echo "📦 Chunk $chunk_num: ${#final_chunk} characters (final chunk)"
        break
      fi

      # Extract a candidate chunk of MAX_CHUNK_SIZE
      local max_end_pos=$((pos + MAX_CHUNK_SIZE))

      # Ensure we don't exceed file boundaries
      if [ $max_end_pos -gt $file_size ]; then
        max_end_pos=$file_size
      fi

      # Get the candidate chunk to search for newlines
      local search_chunk="${content:$pos:$((max_end_pos - pos))}"

      # Find the last newline position in the candidate chunk using parameter expansion
      local actual_end_pos=$max_end_pos # Default fallback

      if [[ "$search_chunk" == *$'\n'* ]]; then
        # Found at least one newline, find the position of the last one
        local before_last_newline="${search_chunk%$'\n'*}"
        local last_newline_pos=${#before_last_newline}
        # Calculate absolute position and include the newline character
        actual_end_pos=$((pos + last_newline_pos + 1))
      else
        # No newline found, use fixed-size split
        log_warning "No newline found in chunk range, using fixed-size split"
        actual_end_pos=$max_end_pos
      fi

      # Ensure we don't exceed file boundaries (double check)
      if [ $actual_end_pos -gt $file_size ]; then
        actual_end_pos=$file_size
      fi

      # Extract the actual chunk
      local chunk_size=$((actual_end_pos - pos))
      local chunk="${content:$pos:$chunk_size}"
      chunks+=("$chunk")

      echo "📦 Chunk $chunk_num: $chunk_size characters (pos: $pos-$actual_end_pos)"

      # Verify chunk is not empty (shouldn't happen, but safety check)
      if [ $chunk_size -eq 0 ]; then
        log_error "Empty chunk created - this indicates a logic error"
        return 1
      fi

      # Move position for next chunk
      pos=$actual_end_pos
      chunk_num=$((chunk_num + 1))
    done

    echo "📦 Created ${#chunks[@]} chunks"
  fi

  # Return chunks array (note: bash can't return arrays, so we use a global)
  CHUNKS=("${chunks[@]}")
}

# =============================================================================
# Translation Function
# =============================================================================

translate_file() {
  local input_file=$1
  local output_dir=${OUTPUT_DIR}
  local output_file="$output_dir/$(basename "$input_file")"

  echo "🌍 Translating $input_file -> $output_file"

  # Validate input file
  if [ ! -r "$input_file" ]; then
    log_error "Cannot read input file: $input_file"
    return 1
  fi

  local existing_italian_content=""
  local system_prompt_with_context="${GEMINI_SYSTEM_PROMPT} ${GEMINI_GLOSSARY}"

  # Check if the translated file exists to use it as context
  if [ -f "$output_file" ]; then
    log_info "Found previous translation in $output_file. Will be added in prompt for anti-churn."

    existing_italian_content=$(cat "$output_file")

    local stability_instruction="

    The content you are about to translate is a chunk of text extracted from a revision of a previously translated document provided below.
    To minimize 'fluctuations' (churn), you must maintain maximum consistency with the stylistic and lexical choices of this context.
    Keep the upper or lower case you find in the italian translation.
    Only alter the translation where required by the changes in the English source file.
        
    Previous complete italian translation:
    ---
    ${existing_italian_content}
    ---
    "
    system_prompt_with_context="${system_prompt_with_context} ${stability_instruction}"

  fi
  
  local file_content=$(cat "$input_file")

  # Create chunks using the new function
  create_chunks "$file_content"
  local chunks=("${CHUNKS[@]}")

  # Translate each chunk with fail-fast behavior
  local translated_chunks=()

  for chunk_index in "${!chunks[@]}"; do
    local chunk="${chunks[$chunk_index]}"
    local chunk_num=$((chunk_index + 1))

    if [ ${#chunks[@]} -gt 1 ]; then
      echo "🌐 Translating chunk $chunk_num/${#chunks[@]} (${#chunk} characters)..."
    else
      echo "🌐 Translating file..."
    fi

    # Prepare API payload for current chunk
    local api_payload=$(jq -n \
      --arg system "$system_prompt_with_context" \
      --arg user_message "${GEMINI_USER_PROMPT} ${chunk}" \
      --arg temperature "$TEMPERATURE" \
      --arg top_k "$TOP_K" \
      --arg top_p "$TOP_P" \
      --arg max_output "$MAX_OUTPUT_TOKENS" \
      '{
        generationConfig: {
          temperature: ($temperature | tonumber),
          topK: ($top_k | tonumber),
          topP: ($top_p | tonumber),
          maxOutputTokens: ($max_output | tonumber),
          thinkingConfig: {
            thinkingBudget: 1024
          }
        },
        systemInstruction: {
          parts: [
            {
              text: $system
            }
          ]
        },
        contents: [
          {
            parts: [
              {
                text: $user_message
              }
            ]
          }
        ]
      }')

    # Retry logic with exponential backoff
    local retry_count=0
    local chunk_success="false"
    local translated_text=""
    local finish_reason=""

    # Retry loop for current chunk
    while [ $retry_count -lt $MAX_RETRIES ] && [ "$chunk_success" != "true" ]; do
      retry_count=$((retry_count + 1))

      if [ $retry_count -gt 1 ]; then
        local retry_delay=$(calculate_retry_delay $retry_count $BASE_RETRY_DELAY)
        if [ ${#chunks[@]} -gt 1 ]; then
          echo "🔄 Chunk $chunk_num - Attempt $retry_count/$MAX_RETRIES (waiting ${retry_delay}s)..."
        else
          echo "🔄 Attempt $retry_count/$MAX_RETRIES (waiting ${retry_delay}s)..."
        fi
        sleep $retry_delay
      fi

      # Make API request with HTTP code extraction
      local http_code=0
      local response=$(curl --location "https://generativelanguage.googleapis.com/v1beta/models/${MODEL}:generateContent?key=${GEMINI_API_KEY}" \
        --header 'content-type: application/json' \
        --data "$api_payload" \
        --silent \
        --connect-timeout 30 \
        --max-time 120 \
        --write-out "HTTPCODE:%{http_code}")

      # Extract HTTP code and response body
      http_code=$(echo "$response" | sed -n 's/.*HTTPCODE:\([0-9]*\).*/\1/p')
      response=$(echo "$response" | sed 's/HTTPCODE:[0-9]*//g')

      # HTTP error handling
      case "$http_code" in
        200)
          # Success case - continue with response processing
          ;;
        400)
          log_error "HTTP 400 - Bad Request for chunk $chunk_num (content too large or invalid)"
          log_info "Chunk size: ${#chunk} characters"
          log_warning "API response: $(echo "$response" | jq -c '.' 2>/dev/null || echo "$response" | head -c 200)"
          break # Don't retry 400 errors - they won't succeed
          ;;
        401|403)
          log_error "HTTP $http_code - Authentication/Authorization error"
          log_warning "Check GEMINI_API_KEY validity"
          return 1 # Exit entire function - auth errors affect all chunks
          ;;
        429)
          log_warning "HTTP 429 - Rate limit exceeded. Waiting ${RATE_LIMIT_DELAY}s..."
          sleep $RATE_LIMIT_DELAY
          continue # Retry this attempt
          ;;
        503)
          log_warning "HTTP 503 - Service temporarily unavailable. Waiting ${SERVICE_UNAVAILABLE_DELAY}s..."
          sleep $SERVICE_UNAVAILABLE_DELAY
          continue # Retry this attempt
          ;;
        *)
          log_warning "HTTP $http_code - Unexpected error"
          log_warning "API response: $(echo "$response" | head -c 200)"
          # Continue with retry logic for unexpected errors
          ;;
      esac

      # Process response only if HTTP 200
      if [ "$http_code" = "200" ]; then
        if echo "$response" | jq empty 2>/dev/null; then
          translated_text=$(echo "$response" | jq -r '.candidates[0].content.parts[0].text // empty')
          finish_reason=$(echo "$response" | jq -r '.candidates[0].finishReason // empty')
          chunk_success="true"
          break
        else
          local chunk_desc=""
          if [ ${#chunks[@]} -gt 1 ]; then
            chunk_desc=" for chunk $chunk_num"
          fi
          log_error "Invalid JSON response$chunk_desc (HTTP $http_code)"
          log_warning "Raw response: $(echo "$response" | head -c 200)..."
        fi
      fi
    done

    # Exit immediately if chunk fails after all retries
    if [ "$chunk_success" != "true" ]; then
      local chunk_desc=""
      if [ ${#chunks[@]} -gt 1 ]; then
        chunk_desc="chunk $chunk_num "
      fi
      log_error "Failed to translate ${chunk_desc}after $retry_count attempts"
      log_error "File translation aborted - no output file created"
      return 1
    fi

    # Check for truncation on the final, successful response and add the marker
    case "$finish_reason" in
        "MAX_TOKENS"|"LENGTH")
            log_warning "Response truncated due to output token limits for chunk $chunk_num"
            log_info "Added truncation marker to chunk $chunk_num"
            translated_text="${translated_text}${TRUNCATION_MARKER}"
            ;;
        "SAFETY"|"RECITATION")
            log_warning "Response blocked by safety filters for chunk $chunk_num. Inserting a placeholder."
            log_info "Added block marker to chunk $chunk_num"
            translated_text="${translated_text}${BLOCK_MARKER}"
            ;;
        "STOP"|"") # Normal completion or empty reason
            ;;
        *)
            if [ -n "$finish_reason" ]; then
                log_warning "Unusual finish reason '$finish_reason' for chunk $chunk_num"
            fi
            ;;
    esac

    # Record successful chunk result
    translated_chunks+=("$translated_text")

    if [ ${#chunks[@]} -gt 1 ]; then
      echo "✅ Chunk $chunk_num translated successfully"
    else
      echo "✅ File translated successfully"
    fi

    # Small delay between chunks to avoid rate limiting (only if multiple chunks)
    if [ ${#chunks[@]} -gt 1 ] && [ $((chunk_index + 1)) -lt ${#chunks[@]} ]; then
      sleep 2
    fi
  done

  # If we reach here, all chunks were translated successfully
  log_info "All ${#chunks[@]} chunks translated successfully"

  # Combine all successfully translated chunks
  local final_translation=""
  for translated_chunk in "${translated_chunks[@]}"; do
    final_translation="${final_translation}${translated_chunk}"
  done

  # Validate final translation is not empty
  if [ -z "$final_translation" ]; then
    log_error "Final translation is empty"
    return 1
  fi

  # Save final translation with atomic write
  local temp_file="${output_file}.tmp"
  if echo "$final_translation" > "$temp_file" && mv "$temp_file" "$output_file"; then
    echo "✅ File translation completed successfully - All ${#chunks[@]} chunks processed"
    echo "📄 Output written to: $output_file"
    return 0
  else
    log_error "Failed to write output file: $output_file"
    rm -f "$temp_file" # Clean up temp file
    return 1
  fi
}

# =============================================================================
# Main Processing Loop
# =============================================================================

success_count=0
failure_count=0
success_files=""
failure_files=""

echo "🚀 Starting translation process..."
start_time=$(date +%s)

for file in "$@"; do
  if [[ $file == *.rst ]] && [ -f "$file" ]; then
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    if translate_file "$file"; then
      success_count=$((success_count + 1))
      success_files="$success_files $file"
    else
      failure_count=$((failure_count + 1))
      failure_files="$failure_files $file"
    fi
    # Pause between files to avoid rate limiting
    sleep 3
  else
    log_warning "Skipped $file: not an RST file or does not exist"
  fi
done

end_time=$(date +%s)
duration=$((end_time - start_time))

# =============================================================================
# Results Summary
# =============================================================================

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 Translation Process Summary"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Files successfully translated: $success_count"
echo "❌ Files with errors: $failure_count"
echo "⏱️ Total processing time: ${duration}s"

if [ $success_count -gt 0 ]; then
  echo ""
  echo "📁 Successfully translated files:"
  for file in $success_files; do
    echo "  • $file"
  done
fi

if [ $failure_count -gt 0 ]; then
  echo ""
  echo "💀 Failed files:"
  for file in $failure_files; do
    echo "  • $file"
  done
fi

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Save results for GitHub Actions workflow
if [ -n "$GITHUB_ENV" ]; then
  {
    echo "SUCCESS_FILES<<EOF"
    echo "$success_files"
    echo "EOF"
    echo "FAILURE_FILES<<EOF"
    echo "$failure_files"
    echo "EOF"
    echo "SUCCESS_COUNT=$success_count"
    echo "FAILURE_COUNT=$failure_count"
    echo "TOTAL_DURATION=$duration"
  } >> "$GITHUB_ENV"
fi

exit 0