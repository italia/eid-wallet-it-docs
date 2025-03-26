.. include:: ../common/common_definitions.rst

.. _log-retention-policy.rst:


General Log Retention Policies
=======================================

The retention of logs is a key element for ensuring security, including fraud prevention, incident detection, system integrity, and compliance with applicable legal obligations. It MUST also be align with the requirements defined in ISO/IEC 27001, in particular wih regard auditability, access control, and secure storage. As long log management may involve the processing of personal data, it also constitutes a measure of accountability under the GDPR, with implications for data minimization, storage limitation, and purpose limitation; for these aspects, reference is made to the relevant provisions of the GDPR and sector-specific regulations.

For all about log handling, Wallet Providers, Credential Issuers, and Relying Parties are considered Organizational Entities. 

Logs related to Wallet data exchange activities (accesses, transactions, credential issuance/revocation) concerning the End User, as the data subject, MUST be retained for a limited period for security, fraud prevention, dispute resolution, and legal obligations.

Organizational Entities are responsible for log retention according to their respective roles. Solutions related to Wallet Providers, Credential Issuers, and Relying Parties MUST implement audit logging for the activities of administrators and service operators with access to data exchange processes and logs.

Unless specific legal obligations dictate otherwise, and with the definition of sector-specific regulation defining appropriate motivations, **the maximum retention period for data logs is 12 months**. Logs MUST be securely stored to ensure integrity and immutability.


GDPR Logs General Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In accordance with the following general principles and in full compliance with them, the retention of logs and personal data made by Organizational Entities MUST adhere to the principles outlined in the GDPR (Article 5), specifically:

- **Lawfulness, Fairness, and Transparency** (Article 5, Paragraph 1, Letter a): Personal data MUST be processed lawfully, fairly, and in a transparent manner in relation to the data subject.
- **Purpose Limitation** (Article 5, Paragraph 1, Letter b): Personal data MUST be collected for specified, explicit, and legitimate purposes and not further processed in a manner that is incompatible with those purposes.
- **Data Minimization** (Article 5, Paragraph 1, Letter c): Personal data MUST be adequate, relevant, and limited to what is necessary in relation to the purposes for which they are processed.
- **Storage Limitation** (Article 5, Paragraph 1, Letter e): Personal data MUST be kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed.
- **Integrity and Confidentiality** (Article 5, Paragraph 1, Letter f): Personal data MUST be processed in a manner that ensures appropriate security, including protection against unauthorized or unlawful processing and against accidental loss, destruction, or damage, using appropriate technical or organizational measures.

Organizational Entities MUST implement appropriate technical and organizational measures to ensure the security of logs and personal data, in compliance with Article 32 of the GDPR.

ISO/IEC 27001 Logging General Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Organizational Entities MUST implement appropriate technical and organization measured in compliance with ISO/IEC 27001 for maintaining an information security management system for monitoring, auditing, and incident response. Key aspects of log handling under ISO/IEC 27001 include the following requirements:

- **A.12.4 Logging and Monitoring**: Organizational Entities MUST produce logs that record exceptions, faults, and information security events. When necessary for security reasons, logs SHOULD capture user activities with a level of detail that is appropriate and sufficient to meet security requirements, ensuring that the data collected is relevant and not excessive. Logs SHOULD be reviewed regularly to ensure that security incidents are identified and addressed promptly.

- **A.12.4.1 Event Logging**: Organizational Entities MUST establish procedures for logging events, including the types of events to be logged, the information to be captured, and the retention period for logs.

- **A.12.4.2 Protection of Log Information**: Organizational Entities MUST be protected against unauthorized access and tampering. This includes implementing access controls, encryption, and integrity checks to ensure that log data remains secure and reliable.

- **A.12.4.3 Administrator and Operator Logs**: Activities of system administrators and operators MUST be logged and reviewed regularly. Organizational Entities MUST detect unauthorized activities and ensures accountability for actions taken on critical systems.

- **A.12.4.4 Clock Synchronization**: All Organizational Entities' systems involved in logging MUST be synchronized to a reliable time source, ensuring accurate timestamps for correlating events across different systems and conducting effective forensic investigations.

- **A.16.1.7 Information Security Incident Management**: Organizational Entities MUST ensure that logs are available and reliable to support incident management processes.


Wallet Provider Log Retention Policy
------------------------------------

Personal data related to the registration and management of Wallet Instances can be retained for up to 12 months after the deactivation/revocation of the Wallet or the associated User account, unless legal obligations require longer retention.

Wallet Provider MUST log the following items:

- Evidences about the User Authentication to the Wallet Provider backends, according to the national regulation pertaining the digital identity systems, if involved (e.g: signed SAML2 Responses, OIDC ID Token). 
- Wallet Attestation Requests.
- Wallet Attestations.
- Holder's requests about the revocation or deactivation of the Wallet Instance.

Credential Issuer Log Retention Policy
--------------------------------------

Credential Issuers define the retention period for Credentials based on sector-specific regulations. In the absence of specific regulations, the retention period for Credentials SHOULD not exceed 12 months after the date of expiration, configured at time of issuance within the metadata of the Issuer Signed part of the Credential.

In detail, Credential Issuers require to be compliant to the items above:

- Credential Issuers MUST log the signed requests made by Wallet Instance during the Credential issuance phase, such as authorization requests and token request (Authorization Server) and the Credential requests at the Credential endpoint (Resource Server).
- Credential Issuers MUST log the evidences about the User Authentication to the Wallet Provider backends, during the authroization phase, according to the national regulation pertaining the digital identity systems, if involved (e.g: signed SAML2 Responses, OIDC ID Token). 
- Credential Issuers MUST log the Issuer signed part of the issued Credentials, such as the Issuer-Signed-JWT using SD-JWT-VC or the MSO using MDoc CBOR.
- Credential Issuer SHOULD NOT log the User personal attributes, such as the Credential disclosure map. 
- Credential Issuers MUST log the Holder's signed revocation request.  

Relying Party Log Retention Policy
----------------------------------

Relying Parties MAY retain data received from the Wallet only for the duration necessary to provide the requested service. The maximum retention period is 24 months after the conclusion of the service, the expiration, or the revocation date of the presented Credentials, unless legal obligations require otherwise.

At the end of the retention period, data MUST be deleted or anonymized.

In detail, Relying Party are required to be compliant with the following items:

- Relying Parties MUST log Wallet's signed presentations, linked to signed presentation requests, containing the Credential Signed part and the Wallet Signed part, such as the Issuer-Signed-JWT and the KB-JWT using SD-JWT-VC.
- Relying Parties SHOULD not log Credetnail presentation disclosure map, where not necessary. 

Wallet Instances Logging Features
---------------------------------

The Commission Implementing Regulation (EU) 2024/2979 establishes detailed rules for the application of Regulation (EU) No 910/2014, inclusing logging in the core functionalities of European Digital Identity Wallets.

Recital (11) of the regulation highlights the critical role of transaction logging as a tool for transparency. Logs enable Wallet Users to effectively monitor their digital identity activities. This transparency aims to improve the user confidence and accountability in digital identity management.

In addition to transparency, logs facilitates the swift and use of information with competent supervisory authorities, as outlined in Article 51 of Regulation (EU) 2016/679 (GDPR). In instances of suspicious behavior by Relying Parties, logs can be quickly provided to authorities, enabling prompt investigation and resolution of potential security threats.

About data export and portability, recital (13) emphasizes the use of data export and portability objects to log person identification data and electronic attestations of attributes issued to a Wallet Instance, supporting the right to data portability. Users are enabled to extract and transfer their data between different Wallet Solutions or recover lost Wallet Instances.

Article 5e, Item 4 of the regulation defines the key features and requirements of the User interface about the navigation of the transaction logs. European Digital Identity Wallets MUST provide a user-friendly, transparent, and traceable dashboard that allows Users to:

- View an up-to-date list of Relying Parties with which they have established a connection, including all data exchanged where applicable.
- Easily request the erasure of personal data by a Relying Party, in accordance with Article 17 of Regulation (EU) 2016/679 (GDPR). Users MUST be able to exercise their right to be forgotten, enhancing their control over personal data.
- Easily report a Relying Party to the competent national data protection authority if an allegedly unlawful or suspicious data request is received, addressing potential data protection violations.

In detail, Wallet Instances MUST log the following items:

- Signed presentation requests issued by Relying Parties.
- Credentials, and disclosed attributes, presented to each Relying Party.

Regulatory References for Log Retention
---------------------------------------

- Regulation (EU) 2016/679 (GDPR)
- Legislative Decree 196/2003 (Personal Data Protection Code)
- ISO/IEC 27001:2024
- Regulation (EU) No 910/2014 (eIDAS)
- National regulations on traffic data retention.
- Provisions of the Data Protection Authority.
