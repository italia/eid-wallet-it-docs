#!/bin/bash
# Certificate chain validation for federation entities

# Convert DER certificates to PEM format for validation
openssl x509 -inform der -in federation_entity.der -out federation_entity.pem
openssl x509 -inform der -in trust_anchor.der -out trust_anchor.pem

# Validate Trust Anchor certificate (self-signed)
echo "Validating Trust Anchor certificate..."
openssl verify -CAfile trust_anchor.pem trust_anchor.pem

# Validate Federation Entity certificate against Trust Anchor
echo "Validating Federation Entity certificate..."
openssl verify -CAfile trust_anchor.pem federation_entity.pem

# Cleanup
rm federation_entity.pem trust_anchor.pem