.. include:: ../common/common_definitions.rst

.. _introduction.rst:

Introduction
************

Over the last decade, digitalization has radically transformed the way citizens and businesses interact with public and private services, introducing new secure, accessible and user-friendly forms of service access. 

In Italy, Decree-Law No. 19 of 2 March 2024, converted, with amendments, by Law No. 56 of 29 April 2024, introduced Article 64-quater of Legislative Decree No. 82 of 7 March 2005, establishing the Italian Digital Wallet System - IT-Wallet System. The IT-Wallet System allows natural or legal persons to access public and private services through the secure presentation of their data on entitlements, delegations, characteristics, licenses or qualifications in the form of Digital Credentials. 

Thanks to the IT-Wallet System, natural and legal persons can directly provide, via their 
wallet, the information required for Authentication in the form of Digital Credentials. Similarly to a physical wallet, the IT-Wallet can contain identity or document-related data, such as a driver's license or health card, as well as a wide range of verifiable digital information, such as a professional qualification, educational diploma, licence or personal qualification. 

What distinguishes the IT-Wallet System from previous Authentication systems is that Digital Credentials refer to characteristics, qualities or properties, already authenticated at source. These Digital Credentials can be used by the User without the Credential Issuers being aware of their use. During the use of the Digital Credentials, no usage information is released to third parties as the relationship is exclusive between the User and the party to whom the Digital Credentials are presented in an informed and transparent way for the User.


Scope 
===========

The following Technical Specifications has two main focus: 

The first one is to define the technical architecture and reference framework that will serve as a guideline for all the parties involved in the development of the IT-Wallet System. 
This documentation defines the national implementation profile of the IT-Wallet System, detailing the technical specifications of its components, as listed below: 

 - Entities of the ecosystem according to `EIDAS-ARF`_; 
 - Infrastructure of trust attesting reliability and eligibility of the participants; 
 - PID and EAAs data schemes and attribute sets;
 - PID/EAA in MDL CBOR format; 
 - PID/EAA in `SD-JWT`_ format; 
 - Wallet Solution general architecture; 
 - Wallet Attestation; 
 - Issuance of PID/EAA according to `OpenID4VCI`_; 
 - Presentation of PID/EAA according to `OpenID4VP`_;
 - Presentation of pseudonyms according to `SIOPv2`_;
 - PID/EAA backup and restore mechanisms;
 - PID/EAA revocation lists. 

The second focus is to provide a clear and structured set of guidelines, resources and design requirements related to the IT-Wallet System elements that impact on the User Experience. 
The document, by distinguishing between mandatory regulatory aspects and good design practices, aims to provide to Public Entities and Private Entities interested in taking part in the IT-Wallet System what is necessary to: 

 - facilitate the understanding and adoption of the Service Model, increasing the number of potential services and usage opportunities for the User; 
 - adopt the IT-Wallet System’s Visual Identity in order to enhance its reliability and recognizability for the User; 
 - ensure design consistency across macro-functionalities and single interactions between the User and the service Touchpoints; 
 - maintain an adequate level of quality, promoting the principles of usability, accessibility and inclusivity. 

Additional guidelines, tools and resources  for the development of the IT-Wallet System Technical Solutions are made available at www.wallet.gov.it.
