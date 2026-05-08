.. include:: ../common/common_definitions.rst

Relying Party Solution Requirements
-----------------------------------

This section lists the requirements to be met by Relying Parties and Relying Party Solutions.

- The Relying Party MUST register with the Federation Authority to obtain both the Access Certificate and the Registration Certificate.
- The Relying Party MUST implement secure mechanisms for handling and processing received Digital Credentials, ensuring the integrity and confidentiality of the Relying Party Solution.
- The Relying Party MUST expose an endpoint for the erasure of personal attributes presented by Users whenever the attributes requested by the Relying Party include a unique identifier of the User (e.g. the "tax_id_code" claim of the PID).
- The Relying Party Solution MUST implement proper revocation procedures for compromised or decommissioned instances.
- The Relying Party Solution MUST maintain an audit trail of Credential verifications while respecting privacy requirements and data protection regulations.
- The Relying Party Solution MUST allow Selective Disclosure mechanisms during presentation scenarios.
- The Relying Party Backend MUST provide a RESTful set of services for registering Relying Party Instances and issuing Access Certificates.
- The Relying Party Instance MUST periodically reestablish trust with the Relying Party through integrity checks and Certificate renewal procedures.
- The Relying Party Instance MUST provide both a Registration Certificate and Access Certificate to Wallet Instances during their interaction to prove the legitimacy and authorization of its requests.
- The Relying Party Instance MUST communicate to Users which attributes are requested and for what purpose during any Credential presentation flow.
- The Mobile Relying Party Instances MUST be compatible and functional on both Android and iOS operating systems and available on the Play Store and App Store, respectively.
- The Mobile Relying Party Instances MUST handle both online and offline presentation scenarios, with appropriate security measures and user notifications.
