.. include:: ../common/common_definitions.rst

.. _log-retention-policy.rst:

General Log and Data Retention Policies
=======================================

The retention of logs and personal data must comply with the principles of the GDPR, with particular attention to data minimization and storage limitation.
Wallet Providers, Credential Issuers, and Relying Parties must implement appropriate security measures.

Logs related to Wallet data exchange activities (accesses, transactions, credential issuance/revocation) concerning the End User, as the data subject, MUST be retained for a limited period for security, fraud prevention, dispute resolution, and legal obligations.


In accordance with the following general principles and in full compliance with them, the retention of logs and personal data in digital identity Wallets MUST adhere to the principles outlined in the GDPR (Article 5), specifically:

- **Lawfulness, Fairness, and Transparency** (Article 5, Paragraph 1, Letter a): Personal data MUST be processed lawfully, fairly, and in a transparent manner in relation to the data subject.
- **Purpose Limitation** (Article 5, Paragraph 1, Letter b): Personal data MUST be collected for specified, explicit, and legitimate purposes and not further processed in a manner that is incompatible with those purposes.
- **Data Minimization** (Article 5, Paragraph 1, Letter c): Personal data MUST be adequate, relevant, and limited to what is necessary in relation to the purposes for which they are processed.
- **Storage Limitation** (Article 5, Paragraph 1, Letter e): Personal data MUST be kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed.
- **Integrity and Confidentiality** (Article 5, Paragraph 1, Letter f): Personal data MUST be processed in a manner that ensures appropriate security, including protection against unauthorized or unlawful processing and against accidental loss, destruction, or damage, using appropriate technical or organizational measures.

Wallet Providers, Credential Issuers, and Relying Parties MUST implement appropriate technical and organizational measures to ensure the security of logs and personal data, in compliance with Article 32 of the GDPR.

Unless specific legal obligations dictate otherwise, and with the definition of sector-specific regulation defining appropriate motivations, the maximum retention period for data logs is 12 months. Logs MUST be securely stored to ensure integrity and immutability.

Wallet Provider Log Retention Policy
------------------------------------

Personal data related to the registration and management of Wallet Instances can be retained for up to 12 months after the deactivation/revocation of the Wallet or the associated User account, unless legal obligations require longer retention.

Credential Issuer Log Retention Policy
--------------------------------------

Credential Issuers define the retention periods for Credentials based on sector-specific regulations. In the absence of specific regulations, the retention period for credentials should not exceed 5 years from the date of issuance.

Relying Party Log Retention Policy
----------------------------------

Relying Parties MAY retain data received from the Wallet only for the duration necessary to provide the requested service. The maximum retention period is 24 months after the conclusion of the service, the expiration, or the revocation date of the presented Credentials, unless legal obligations require otherwise.

At the end of the retention period, data MUST be deleted or anonymized.

General Responsibilities for Log Retention
------------------------------------------

Wallet Providers, Credential Issuers, and Relying Parties are responsible for data retention according to their respective roles. Solutions related to Wallet Providers, Credential Issuers, and Relying Parties MUST implement audit logging for the activities of administrators and service operators with access to data exchange and logs.

Regulatory References for Log Retention
---------------------------------------

- Regulation (EU) 2016/679 (GDPR)
- Legislative Decree 196/2003 (Personal Data Protection Code)
- Regulation (EU) No 910/2014 (eIDAS)
- National regulations on traffic data retention.
- Provisions of the Data Protection Authority.
