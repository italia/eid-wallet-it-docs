# Topic 55 - Certificate Transparency

| **Requirement ID** | **Legacy ID** | **Description** | **Status** |
|-------------------|---------------|------------------|------------|
| CT_01 |  | An Access CA issuing access certificates SHALL register these in a CT log according to RFC 9162, if such a log is available for access certificates. | 🟡 |
| CT_02 |  | An Access CA issuing access certificates SHALL describe in its CPS how it logs all access certificates. | 🟡 |
| CT_03 |  | In case a CT log provider for access certificates is available, all Access CAs SHALL act as monitors in the CT ecosystem. Access CAs SHOULD still monitor the CT logs in situations of temporary unav... | 🟡 |
| CT_04 |  | An Access CA SHALL include at least one Signed Certificate Timestamp (SCT) in each access certificate. | 🟡 |
| CT_05 |  | When verifying an access certificate during PID or attestation issuance or presentation, a Wallet Unit SHALL also verify that the access certificate includes at least one valid Signed Certificate T... | 🟡 |
| CT_06 |  | If an access certificate does not include a valid SCT, a Wallet Unit SHALL handle this as a failure or Relying Party authentication, in compliance with all requirements in [[Topic 6](./annex-2.02-h... | 🟡 |