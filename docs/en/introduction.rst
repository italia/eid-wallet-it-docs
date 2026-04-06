.. include:: ../common/common_definitions.rst


Introduction
============

In Italy, Decree-Law No. 19 of 2 March 2024, converted, with amendments, by Law No. 56 of 29 April 2024, introduced Article 64-quater of Legislative Decree No. 82 of 7 March 2005, establishing the Italian Digital Wallet System - IT-Wallet System. The IT-Wallet System allows **citizens and businesses** to access public and private services through the secure presentation of Digital Credentials, attesting to entitlements, delegations, characteristics, licenses or qualifications. Article 64-quater also provides for the adoption of one or more implementing decrees (decreti attuativi) to define the rules governing the operation of the IT-Wallet System, including the roles of the entities involved, technical and security requirements, and principles of economic sustainability, of which these Technical Specifications – drafted through an open and collaborative process – form an integral part.

Thanks to the IT-Wallet System, **citizens and businesses** can provide, via their Wallet, the information required for accessing services provided by public and private entities in the form of Digital Credentials. Similarly to a physical wallet, the IT-Wallet can contain identity or document-related data, such as a driver's license or health card, as well as a wide range of verifiable digital information, such as a professional qualification, educational diploma, licence or verifiable attribute.

The main roles in the Wallet ecosystem are listed as follow:

- **Credential Issuers**: parties who issue Digital Credentials to Users;
- **Relying Parties**: parties who request Digital Credentials presentations to the User, for Authentication and authorization purposes;
- **Users**: individuals who own a Wallet Instance and have control over the Digital Credentials they can request, acquire, store, and present to Relying Parties;

In this model, the Credential Issuer (e.g., an educational institution) provides Digital Credentials to the User, who can store them in their Wallet Instance.
The Wallet Instance is typically provided as a mobile application on the User's smartphone. 

What distinguishes this new approach from previous identity access management systems is that Digital Credentials refer to characteristics, qualities or properties, already authenticated at source. These Digital Credentials can be used by the User without the Credential Issuers being aware of their use. During the use of the Digital Credentials, no usage information is released to third parties as the relationship is exclusive between the User and the Relying Party, in a transparent and informed manner.
A phased experimentation process validates technical components, user experience, and interoperability, and supports progressive alignment with the European Digital Identity Wallet (EUDI Wallet).

Other key elements that characterize this new Digital Identity Wallet paradigm include:

- **Privacy and control**: Wallets enable individuals to maintain control over the information provided within the presented Credentials. They can choose what attributes or Credentials to present and to whom;
- **Security**: Wallets leverage cryptographic mechanism for the integrity and the security of exchanged data. This avoids identity theft, fraud, and unauthorized access;
- **Interoperability**: Wallets promote interoperability by enabling different systems and organizations to recognize and verify identities, enabling trusted interactions between individuals, organizations, and even across borders;
- **Efficiency and cost reduction**: Individuals can easily manage their own Credentials, avoid handling multiple identity tokens, and reduce repetitive identity verification processes.

Scope
-----

These Technical Specifications complement the Guidelines under Article 64-quater of Legislative Decree No. 82/2005 (CAD). Once formally adopted, they become part of the regulatory framework for the IT-Wallet System and are updated as experimentation, legislation, and requirements evolve.

Regardless of role, implementers should note the following:

- **Regulatory alignment**: the specifications implement the applicable national and European framework and MUST be considered when building IT-Wallet Technical Solutions.
- **Open and living document**: the specifications are developed collaboratively, published as open documentation, and revised as the ecosystem matures.
- **Requirements vs good practice**: the text distinguishes mandatory rules from recommended practice, including for **Security**, **Privacy**, and **Interoperability**.

The specifications also bundle User Experience recommendations, design resources, and the technical architecture for Primary Actors. Official Resources for design and development are listed in :ref:`official-resources:Official Resources` and updated over time.

For role-based reading paths, see :ref:`introduction:How to Read the Specification`.

Normative Language and Conventions
----------------------------------

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.

.. include:: how-to-read-spec.rst


