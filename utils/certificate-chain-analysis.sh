#!/bin/bash
# Certificate chain analysis for federation entities
# Array containing certificates in DER format encoded in Base64
certificate_chain=(
    "MIIDyzCCA3GgAwIBAgI..." # Federation Entity Certificate
    "MIIDQzCCAuigAwIBAgI..." # Trust Anchor Certificate
)

# Display first certificate (Federation Entity)
echo "===================================="
echo " Federation Entity Certificate Analysis"
echo "===================================="
echo
echo "${certificate_chain[0]}" | base64 -d > federation_entity.der
openssl x509 -in federation_entity.der -inform DER -text -noout

# Display second certificate (Trust Anchor)
echo "====================================="
echo " Trust Anchor Certificate Analysis"
echo "====================================="
echo
echo "${certificate_chain[1]}" | base64 -d > trust_anchor.der
openssl x509 -in trust_anchor.der -inform DER -text -noout

# Cleanup temporary files
rm federation_entity.der trust_anchor.der
