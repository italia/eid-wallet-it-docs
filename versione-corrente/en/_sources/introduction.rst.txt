.. include:: ../common/common_definitions.rst

.. _introduction.rst:

Introduction
************

Over the last decade, digitalization has radically transformed the way citizens and businesses interact with public and private services, introducing new secure, accessible and user-friendly forms of service access. 

In Italy, Decree-Law No. 19 of 2 March 2024, converted, with amendments, by Law No. 56 of 29 April 2024, introduced Article 64-quater of Legislative Decree No. 82 of 7 March 2005, establishing the Italian Digital Wallet System - IT-Wallet System. The IT-Wallet System allows natural or legal persons to access public and private services through the secure presentation of Digital Credential, attesting to entitlements, delegations, characteristics, licenses or qualifications.  Article 64-quater also provides for the adoption of one or more implementing decrees (decreti attuativi) to define the rules governing the operation of the IT-Wallet System, including the roles of the entities involved, technical and security requirements, and principles of economic sustainability, of which these Technical Specifications – drafted through an open and collaborative process – form an integral part.

Thanks to the IT-Wallet System, natural and legal persons can directly provide, via their 
wallet, the information required for Authentication in the form of Digital Credentials. Similarly to a physical wallet, the IT-Wallet can contain identity or document-related data, such as a driver's license or health card, as well as a wide range of verifiable digital information, such as a professional qualification, educational diploma, licence or certified attribute. 

What distinguishes the IT-Wallet System from previous Authentication systems is that Digital Credentials refer to characteristics, qualities or properties, already authenticated at source. These Digital Credentials can be used by the User without the Credential Issuers being aware of their use. During the use of the Digital Credentials, no usage information is released to third parties as the relationship is exclusive between the User and the service provider, in a transparent and informed manner.
The development of the IT-Wallet System includes a phased experimentation process, aimed at testing the Wallet and assessing its impact in real-world contexts. This process is designed to validate technical components, user experience elements, and interoperability mechanisms, while ensuring a progressive and controlled adoption of the System. Moreover, it supports the continuous improvement of the IT-Wallet and its gradual alignment with the European Digital Identity Wallet (EUDI Wallet), both in terms of architecture and compliance with evolving European specifications.

Scope 
=====

These Technical Specifications are intended to complement the Guidelines provided for in Article 64-quater of Legislative Decree No. 82/2005 (CAD). Both the Guidelines and these Technical Specifications, once formally adopted, will become part of the regulatory framework for the IT-Wallet System. They will be periodically updated, where necessary, in light of the results of the experimentation phase, the adoption of new national or European legislative acts, and evolving requirements in terms of security and interoperability. These Technical Specifications pursue two main objectives and represent a core component of the implementation framework for the IT-Wallet System.

The first one is to provide a clear and structured set of recommendations, resources and design requirements related to the IT-Wallet System elements that impact on the User Experience. 
The document, by distinguishing between mandatory regulatory aspects and good design practices, aims to provide to public entities and private entities interested in taking part in the IT-Wallet System what is necessary to: 

 - facilitate the understanding and adoption of the Service Model, increasing the number of potential services and usage opportunities for the User; 
 - adopt the IT-Wallet System’s Visual Identity in order to enhance its reliability and recognizability for the User; 
 - ensure design consistency across macro-functionalities and single interactions between the User and the service Touchpoints; 
 - maintain an adequate level of quality, promoting the principles of usability, accessibility and inclusivity. 


The second focus is to define the technical architecture and reference framework that will serve as a guideline for all the parties involved in the development of the IT-Wallet System. 
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
 - PID/EAA backup and restore mechanisms;
 - PID/EAA revocation lists. 

Additional documentation, tools and resources - hereinafter defined Official Resources - for the design and development of the IT-Wallet System Technical Solutions will be made available on the upcoming website http://www.wallet.gov.it. 

