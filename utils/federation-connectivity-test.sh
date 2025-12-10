#!/bin/bash
# Federation certificate infrastructure connectivity test

# Test Trust Anchor certificate endpoint
ta_cert_url="https://trust-anchor.eid-wallet.example.it/pki/ta.cer"
if curl -f -s "$ta_cert_url" > /dev/null; then
    echo "Trust Anchor certificate endpoint: ACCESSIBLE"
else
    echo "Trust Anchor certificate endpoint: FAILED"
fi

# Test CRL distribution endpoints
ta_crl_url="https://trust-anchor.eid-wallet.example.it/pki/ta.crl"
if curl -f -s "$ta_crl_url" > /dev/null; then
    echo "Trust Anchor CRL endpoint: ACCESSIBLE"
else
    echo "Trust Anchor CRL endpoint: FAILED"
fi
