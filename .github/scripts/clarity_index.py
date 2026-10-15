#!/usr/bin/env python3
"""Editorial clarity index for the published specification.

The index runs from 0 to 100. Higher is clearer. Prose is scored after
build directives, literals, and links are removed. A directive block,
including its options and indented body, is markup for the HTML build and
is not editorial. A document starts at 100 and loses:

- up to 40 points for the share of sentences longer than 35 words
  (1.2 points per percent, capped)
- up to 30 points for semicolons per 1 000 words (6 points each, capped)
- up to 30 points for sentences with two or more normative keywords,
  per 1 000 words (12 points each, capped)

Exit status is 1 when a scored document falls below its baseline, or when
a changed document scores under the threshold. Unchanged documents already
under the threshold are reported and do not fail the run.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
BASELINE_PATH = ROOT / ".github" / "clarity-baseline.json"
THRESHOLD = 55.0

EN_KEYWORDS = re.compile(
    r"\b(MUST NOT|MUST|REQUIRED|SHALL NOT|SHALL|SHOULD NOT|SHOULD|"
    r"NOT RECOMMENDED|RECOMMENDED|MAY|OPTIONAL)\b"
)
IT_KEYWORDS = re.compile(
    r"\b(NON DEVONO|NON DEVE|DEVONO|DEVE|NON DOVREBBERO|NON DOVREBBE|"
    r"DOVREBBERO|DOVREBBE|NON RACCOMANDATO|RACCOMANDATO|POSSONO|PUÒ|"
    r"OBBLIGATORIO|OPZIONALE)\b"
)

# Markup that drives the HTML build. The directive line, its options, and
# its indented body are not editorial prose. Names are matched case-insensitively.
DROP_DIRECTIVES = frozenset({
    "note", "warning", "attention", "important", "hint", "tip", "seealso",
    "admonition", "caution", "danger", "error",
    "figure", "image",
    "include", "toctree", "only", "raw", "contents", "highlight", "role", "rubric",
    "list-table", "csv-table",
    "code-block", "code", "literalinclude", "parsed-literal", "plantuml",
})

DIRECTIVE_RE = re.compile(r"^(\s*)\.\.\s+([A-Za-z0-9_-]+)::")
TARGET_RE = re.compile(r"^\s*\.\.\s+_")
COMMENT_RE = re.compile(r"^\s*\.\.\s+\S")


def _indent(line: str) -> int:
    return len(line) - len(line.lstrip(" \t"))


def strip_rst(text: str) -> str:
    lines: list[str] = []
    skip_deeper_than: int | None = None
    for line in text.splitlines():
        if skip_deeper_than is not None:
            if line.strip() == "" or _indent(line) > skip_deeper_than:
                continue
            skip_deeper_than = None

        directive = DIRECTIVE_RE.match(line)
        if directive and directive.group(2).lower() in DROP_DIRECTIVES:
            skip_deeper_than = _indent(line)
            continue
        if TARGET_RE.match(line):
            continue
        if COMMENT_RE.match(line) and directive is None:
            skip_deeper_than = _indent(line)
            continue
        lines.append(line)
    prose = "\n".join(lines)
    prose = re.sub(r"``.*?``", " TOKEN ", prose)
    prose = re.sub(r":[a-zA-Z0-9_-]+:`[^`]*`", " REF ", prose)
    prose = re.sub(r"`[^`]+`_", " REF ", prose)
    prose = re.sub(r"https?://\S+", " URL ", prose)
    prose = re.sub(r"^\s*\.\..*$", "", prose, flags=re.M)
    prose = re.sub(r"^[=^\"'.-]{3,}\s*$", "", prose, flags=re.M)
    prose = re.sub(r"^\s*[\*\-]\s+", "", prose, flags=re.M)
    return prose


def sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+", text)
    found: list[str] = []
    for part in parts:
        cleaned = re.sub(r"\s+", " ", part).strip()
        if len(cleaned.split()) >= 4:
            found.append(cleaned)
    return found


def score_text(text: str, keywords: re.Pattern[str]) -> float | None:
    prose = strip_rst(text)
    found = sentences(prose)
    if len(found) < 8:
        return None
    lengths = [len(item.split()) for item in found]
    long_count = sum(1 for length in lengths if length > 35)
    word_count = sum(lengths)
    semicolons = prose.count(";")
    stacked = sum(1 for item in found if len(keywords.findall(item)) >= 2)
    percent_long = 100.0 * long_count / len(found)
    semicolons_per_thousand = 1000.0 * semicolons / max(word_count, 1)
    stacked_per_thousand = 1000.0 * stacked / max(word_count, 1)
    clarity = 100.0
    clarity -= min(40.0, 1.2 * percent_long)
    clarity -= min(30.0, 6.0 * semicolons_per_thousand)
    clarity -= min(30.0, 12.0 * stacked_per_thousand)
    return round(max(0.0, clarity), 1)


def documents() -> list[tuple[str, float]]:
    rows: list[tuple[str, float]] = []
    for language, keywords in (("en", EN_KEYWORDS), ("it", IT_KEYWORDS)):
        for path in sorted((DOCS / language).glob("*.rst")):
            if path.name.startswith("test-plans"):
                continue
            score = score_text(path.read_text(encoding="utf-8"), keywords)
            if score is None:
                continue
            rows.append((f"docs/{language}/{path.name}", score))
    return rows


def load_baseline() -> dict[str, float]:
    if not BASELINE_PATH.is_file():
        return {}
    payload = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
    return {key: float(value) for key, value in payload["scores"].items()}


def write_baseline(rows: list[tuple[str, float]]) -> None:
    payload = {
        "threshold": THRESHOLD,
        "scores": {path: score for path, score in rows},
    }
    BASELINE_PATH.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def read_changed(path: Path | None) -> set[str]:
    if path is None:
        return set()
    names: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        name = line.strip()
        if name.startswith("docs/") and name.endswith(".rst") and "test-plans" not in Path(name).name:
            names.add(name)
    return names


def append_summary(text: str) -> None:
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary:
        return
    with open(summary, "a", encoding="utf-8") as handle:
        handle.write(text)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-baseline", action="store_true")
    parser.add_argument("--changed-from", type=Path)
    args = parser.parse_args()

    rows = documents()
    if args.write_baseline:
        write_baseline(rows)
        print(f"Wrote {len(rows)} scores to {BASELINE_PATH.relative_to(ROOT)}")
        return 0

    baseline = load_baseline()
    changed = read_changed(args.changed_from)
    failures: list[str] = []
    grandfathered: list[str] = []

    print(f"{'score':>6}  {'base':>6}  path")
    for path, score in sorted(rows, key=lambda item: (item[1], item[0])):
        base = baseline.get(path)
        base_text = "-" if base is None else f"{base:.1f}"
        print(f"{score:6.1f}  {base_text:>6}  {path}")
        if base is not None and score + 0.05 < base:
            failures.append(f"{path} fell from {base:.1f} to {score:.1f}")
        if path in changed and score < THRESHOLD:
            failures.append(f"{path} scores {score:.1f}, under {THRESHOLD:.0f}")
        elif path not in changed and score < THRESHOLD:
            grandfathered.append(f"{path} {score:.1f}")

    for path in sorted(changed - {item[0] for item in rows}):
        if path not in baseline:
            continue
        failures.append(f"{path} is changed and is no longer scored")

    summary = [
        "# Editorial clarity index",
        "",
        f"Threshold: {THRESHOLD:.0f}. Changed documents under the threshold fail.",
        f"Grandfathered documents under the threshold: {len(grandfathered)}.",
        "",
    ]
    if grandfathered:
        summary.append("## Unchanged documents under the threshold")
        summary.append("")
        summary.extend(f"- {item}" for item in grandfathered)
        summary.append("")
    if failures:
        summary.append("## Failures")
        summary.append("")
        summary.extend(f"- {item}" for item in failures)
        summary.append("")
    append_summary("\n".join(summary))

    if failures:
        print("\nClarity check failed:", file=sys.stderr)
        for item in failures:
            print(f"- {item}", file=sys.stderr)
        return 1
    print(f"\nClarity check passed. {len(grandfathered)} unchanged documents are under {THRESHOLD:.0f}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
