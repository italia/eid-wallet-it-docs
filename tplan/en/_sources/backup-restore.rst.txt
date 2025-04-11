.. include:: ../common/common_definitions.rst

.. _backup-restore.rst:

Backup and Restore
++++++++++++++++++
The **Backup and Restore** functionality becomes relevant when the User wants to change device and/or Wallet Solution in order to access the previously issued Digital Credentials again.

- The mobile device has been **lost**, **stolen**, **damaged**, or **compromised** (e.g., due to unauthorized access).
- The User replaces an existing Wallet Instance with a new instance of the same Wallet Solution.
- The User has changed their mobile device and needs to set up the Wallet Solution on the new device.
- The User performs a factory reset on the current phone and needs to set up the Wallet Solution again.

.. note::
  
  For Wallet Solutions based on the IT Wallet technical specifications, the migration to a different Wallet Solution (known as data portability) can be supported following the backup and restore functionality described in this section.
  

Backup Flow
-----------

.. _fig_Backup_flow:
.. figure:: ../../images/Backup_flow.svg
   :name: Sequence Diagram for Wallet Instance Backup
   :alt: The figure illustrates the sequence diagram for backup flow, with the steps explained below.
   :target: https://www.plantuml.com/plantuml/png/VP5HRzGm3CVVyodClMn8j1KmU9YcqxPZe8bDEkaqyG1eIbFlQaYJAd4uAhJlJj96WuvZUMhj_y_-spxrB1s7JejdP9GE3KBBtFlZgd9oLsw9sr07ZqvPmsYuLBQhUYrDOWhFZQQwMXqLwnIwkRwgEkaPNGpThY8XoQ0h-rHVICNMmKsi1TB38dqiXDWCKT_TdjjW6kc6mvtK6dbZTM2oviMaE_3m3d-GmiLp-2KWlltOfV4iZSA8VHe3a2CPpE_1sM6Wt24A6TsTJCezkbggxw4_wsc3Blc8rFaOWhFr9UHW9k_5dEriJHetR9tS9l1w_Cy3mPLLKaFE9fUvnhqG1t3nizUaY47BmGO6sNmBdZiq37VMGMyzfIsHsOfP5oW-jzGqQBuMIvYlHeXnt28c0i4nB4xgvSiIyZGhXv5YajgVLFLo8QBc96aVBs02NvNm0GqwoGWVSO1rwwJ7FsWYKxj9_ReSvzmZVLmT_j_og4mcKyCBezpGCpQGpRydZK_K2pHLU5F-Y-vp_8GKlXY8QTWHjx1sjkkdW_oL6-zQhRGDJRvkzlQm_ld5fePlInZ1ENAAfWcT_Wq0
   
   Backup flow.

Below, the description of the steps of :numref:`fig_Backup_flow`:

**Step 1**: The User selects the option to back up Credentials stored within the Wallet Instance. 

**Steps 2-3**: The Wallet Instance using the backup APIs randomly selects 10 key phrases from a pre-generated list of words and displays it to the User. 
The User MUST securely store the key phrase chosen from those proposed by the system (e.g., in a password manager or a physical safe) as they are critical for restoring the backup.

.. note::
  
  As highlighted in the ARF, encryption is necessary because the backup file is considered sensitive. Even if an attacker only knows the Issuer identifiers, they can infer the different types of Digital Credentials, which constitutes a violation of User privacy.

.. note::
  
  To extract the key from the list of selected words a key derivation function MUST be applied. Password-Based-Key-Derivation Function 2 (PBKDF2) is among the mostly used ones based on `RFC 2898`_ and it is recommended by the `NIST 800-132 <https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-132.pdf>`_. There are other relevant techniques that are available and used widely, such as Bcrypt, Scrypt, and Argon2. More details on this approach can be found `here <https://cryptobook.nakov.com/mac-and-key-derivation/kdf-deriving-key-from-password>`_.

.. note::
  
  The work factor for PBKDF2 is implemented through an iteration count, which should set differently based on the internal hashing algorithm used. The recommended value for ``SHA-256`` hashing algorithim is 600000 iterations as stated in the `OWASP Password Storage Cheatsheet <https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#pbkdf2>`_.


**Step 4**: The Wallet Instance performs the operations below to create the backup JWT entry for the backup file. 
 
- For each of the HW bound key Credentials, add the Credential Issuer identifier and the ``credential_configuration_id`` as an entry in the backup JWT. 
- Sign the backup JWT using the private key that its public key is attested within the Wallet Attestation. The related public key that is attested by the Wallet Provider is provided within the Wallet Attestation (``cnf`` claim). The Wallet Instance MUST verify the validity of the Wallet Attestation before signing the backup JWT.
- Add the signed backup JWT as an entry to the backup file. 
- Encrypt the backup file using the provided key phrase. 

.. note::

  The Backup JWT MAY contain transaction history for each Credential entry within the ``credentials_backup`` claim.

  

**Step 5**: The User will be prompted to choose a storage option for securely storing the backup file. Options may include native storage or external storage solutions, such as cloud storage, USB devices, e-mail delivery or any other.

**Step 6**: In the case where the User prefers the native storage, the backup file is stored on the User device.

A non-normative example of the backup JWT is as the following:
 
 .. code-block::
  
  { 
    "alg": "ES256",   
    "typ": "wallet-unit-credentials-backup+jwt",    
  }
  .
  {
    "timestamp":"2024-12-13T16:35:06+01:00",
    "wallet_provider_id":"https://wallet-provider.example.org/",
    "wallet_instance_version":"v1.0",
    "wallet_attestation":"eyJhbGciOiJFUzI1NiIsImVVfQz.eyJpc3MiOiAiaH...LCAibmJ",
    "credentials_backup": {  
        "https://issuer.example.org/v1.0/mdl": ["org.iso.18013-5.1.mDL"],
        "https://eaa-provider.example.org/": ["dc_sd_jwt_EuropeanDisabilityCard"]
     },
  }

The JOSE header of the backup JWT MUST contain the following REQUIRED parameters:

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **JOSE header**
      - **Description**
      - **Reference**
    * - **alg**
      - A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms listed in the Section `Cryptographic Algorithms <algorithms.html>`_ and MUST NOT be set to ``none`` or any symmetric algorithm (MAC) identifier.
      - :rfc:`7516#section-4.1.1`.
    * - **typ**
      -  It MUST be set to ``wallet-unit-credentials-backup+jwt``
      - N/A

The body of backup JWT contains the following REQUIRED claims:

.. list-table::
    :widths: 20 60 
    :header-rows: 1

    * - **Claim**
      - **Description**
    * - **timestamp**
      - UNIX timestamp with the time of backup file creation. This value is updated every time a new credential entry is added to the backup file.
    * - **wallet_provider_id**
      - It MUST be set to the unique identifier of the Wallet Provider.
    * - **wallet_instance_version**
      - It MUST be set to  the version of the Wallet Solution that has been backed up.
    * - **wallet_attestation**
      - It MUST be set to a value containing the Wallet Attestation JWT. 
    * - **credentials_backup**
      - Object that describes specifics of the Credential that are backupped. This object contains a list of name/value pairs, where each name is a unique identifier of the Credential Issuer. This identifier is used to initiate the issuance phase. The value is an array of unique strings. Each string corresponds to the ``credential_configuration_id`` that identifies the specific Digital Credential that was issued.


Restore flow for Hardware Binding Credential
--------------------------------------------

.. _fig_Restore_flow:
.. figure:: ../../images/Restore_Flow.svg
   :name: Sequence Diagram for Wallet Instance Restore
   :alt: The figure illustrates the sequence diagram for restore flow, with the steps explained below.
   :target: https://www.plantuml.com/plantuml/png/TP5DRnCn48Rl-ok6N9fAP5T0-L0LHVrea2fQ4OWg3e2gsVKqCNZjbJrk6w7-T-or5TYssPCpVfzd9kCZnsZPjwfu8NMZl21OCtVkiAeitfKhoMjVUqUsCPf9SzcOjkeKwiXC70ibw-hqOBA8fQlBYwf5nsH3wVeq42WrsRAB_W8RDXQkWWlGmIWUHaMnt8HyUtrYl1PeD-CxL8fuQPHdQVJBbDjpS4Qtig7HFlmf87pFO-VQCUg60lQjBq2kP31_syd6NkOE8SXaRp0cdydLsFpstN4dbsJZ784wwKjml3Y7NCpaGr4CuTRKKj6IZSLL92_xt_aVmOLfK46wJMCcoSDsD_Dx7fyxvya6E1r2gs8FvlUTaeraKBWndW75B--u9SrmOonqnicuHAbNnM06c7nVIo58_vpCOBYvgFrA2YFdrh9pHR-TaFCI3c4qhMUlof1mmKIGbZojwjaevQQJVxdN9IoiQJi6Dd3LAOC2yj8-IaK3QWR30PFXJGbBKjJm_npS12dau5QIHqpSGT_vLWg2kMxifcCI0mLg4MuuK9ze0ukrHKSkkRoCfiVldRnlozs-fwR7ZjtUToMSKVP65dxeKCqDaYmzEpnvhoHuNyBdcb5gk2H6WOn3RBg3-r12du3nb_tv_BXde3WYBNoh_W80
   
   Restore flow.

Considering that the User has initialized the new Wallet Instance and it is in active state by obtaining a new PID, this specification relaxes the requirement of the ARF concerning the addition of the PID in the backup file. 
Below, the description of the steps of :numref:`fig_Restore_flow`:

**Steps 1-6**: The User wants to restore the Digital Credentials using the backup previously created with their Wallet Instance. 
The User selects `restore Digital Credentials backup` in the Wallet Instance app and a prompt with the import function is provided to the User. The backup file to be imported can be provided using a local storage or a remote location using a cloud storage as well, and therefore submit the recovery key phrases. 
To check the authenticity of the file, the Wallet Instance MUST verify the backup JWT's signature to ensure its authenticity. To do this, it first extracts the Wallet Attestation JWT from ``wallet_attestation`` claim and obtains the related public key using the Wallet Attestation (``cnf`` claim).

**Steps 7-8**: The Wallet Instance for each HW binding credentials entry in the payload of the backup JWT performs the following steps:

- It extracts the Credential Issuer identifier and the ``credential_configuration_id`` from the entry. The former is used to identify the Issuer and obtains its metadata, while the latter will be used to signal the Credential type to the Credential Issuer. 
- Using the Issuer identifier the Wallet Instance obtains the metadata of the Credential Issuer and makes a re-issuance request to the Credential Issuer by providing the new cryptographic binding with the Credential. 

.. note::
  
  The Wallet Instance MUST not check the expiration of the Wallet Attestation as its main purpose is to enable the Wallet Instance to verify the authenticity of the backup file by ensuring it has been created and signed by a Wallet Instance of a specific Wallet Provider.

 

.. _ARF: https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework

.. _RFC 2898: http://tools.ietf.org/html/rfc2898.html


