#!/bin/bash
# Certificate revocation verification for federation entities

# Extract certificate serial number
certificate_serial=$(openssl x509 -in certificate.der -inform DER -noout -serial | \
                  cut -d= -f2)

# Normalize serial number (remove leading zeros, convert to lowercase)
normalized_serial=$(echo "$certificate_serial" | sed 's/^0*//' | tr '[:upper:]' '[:lower:]')

echo "Certificate Serial Number: $normalized_serial"

# Extract CRL URL and download
crl_url=$(openssl x509 -in certificate.der -inform DER -text -noout | \
          grep "URI:" | sed 's/.*URI://')
curl -s -O "$crl_url"
crl_file=$(basename "$crl_url")

# Validate CRL signature against Trust Anchor
echo "Validating CRL signature..."
openssl crl -in "$crl_file" -inform DER -noout -text -CAfile trust_anchor.pem

# Extract revoked serial numbers from CRL
revoked_serials=$(openssl crl -in "$crl_file" -inform DER -text -noout | \
                 grep 'Serial Number' | \
                 sed 's/.*Serial Number: //' | \
                 sed 's/^0*//' | \
                 tr '[:upper:]' '[:lower:]')

# Check if certificate is revoked
if echo "$revoked_serials" | grep -q "$normalized_serial"; then
    echo "Certificate Status: REVOKED"
    exit 1
else
    echo "Certificate Status: VALID"
    exit 0
fi
