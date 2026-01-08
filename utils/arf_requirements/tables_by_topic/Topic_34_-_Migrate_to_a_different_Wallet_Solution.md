# Topic 34 - Migrate to a different Wallet Solution

| **Requirement ID** | **Legacy ID** | **Description** | **Status** |
|-------------------|---------------|------------------|------------|
| Mig_01 |  | A Wallet Unit SHALL include and keep up-to-date a Migration Object, containing the following information: - The contents of the log for all transactions executed through the Wallet Unit, as listed ... | 🟡 |
| Mig_02 |  | The Migration Object SHALL comply with all requirements in [Technical Specification 10](../../technical-specifications/ts10-data-portability-and-download-(export).md). | 🟡 |
| Mig_03 |  | For each PID or device-bound attestation that is issued to it, a Wallet Unit SHALL add to the Migration Object all data necessary to request issuance of that PID or attestation once again. This SHA... | 🟡 |
| Mig_03a |  | For each non-device bound attestation that is issued to it, a Wallet Unit SHALL add to the Migration Object one of the following: either all data necessary to request issuance of that attestation o... | 🟡 |
| Mig_03b |  | If the User deletes a PID or attestation from their Wallet Unit, the Wallet Unit SHALL delete the corresponding entry from the Migration Object. | 🟡 |
| Mig_04 |  | The Wallet Unit SHALL store the Migration Object in an external storage or remote storage location of the User's choice, from among the storage options supported by the Wallet Unit, in such a way t... | 🟡 |
| Mig_05 |  | The Wallet Unit SHALL store the Migration Object in such a way that its confidentiality, integrity, and authenticity is protected and that it is protected against use by others than the User. *Note... | 🟡 |
| Mig_06 |  | Directly after installation of a new Wallet Instance, the Wallet Instance SHALL enable the User to import a Migration Object from an external storage or remote storage location indicated by the Use... | 🟡 |
| Mig_07 |  | When importing a Migration Object, for each PID and device-bound attestation listed in the Migration Object, the Wallet Unit SHALL enable the User to select that PID or attestation. When a PID or d... | 🟡 |
| Mig_07a |  | When importing a Migration Object, for each non device-bound attestation listed in the Migration Object, the Wallet Unit SHALL enable the User to select that attestation. When an attestation is sel... | 🟡 |
| Mig_08 |  | Empty | 🟡 |
| Mig_09 |  | Empty | 🟡 |
| Mig_10 |  | Empty | 🟡 |
| Mig_12 |  | Empty | 🟡 |
| Mig_13 |  | Empty | 🟡 |
| Mig_14 |  | Empty | 🟡 |
| Mig_15 |  | Empty | 🟡 |
| Mig_16 |  | Empty | 🟡 |