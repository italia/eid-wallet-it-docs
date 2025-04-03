Functionalities
################

The IT-Wallet System provides Users with a simpler, faster, and more secure way to access services. This service is delivered through the use of a Wallet Solution, whose User Experience is structured into three main phases: pre-use, use, and post-use. 

..  figure:: ../../images/UX-phases-usage.svg
    :alt: User Experience phases of Wallet usage
    :width: 100%
 	*User Experience phases of Wallet usage*


The following sections focus on the usage and post-usage phases. They define the functional requirements supporting the User Experience for the Activation, Acquisition, Presentation, Management, and Deactivation phases, along with interaction requirements related to error management, assistance requests, and feedback collection. 

Each section includes references to the supporting resources and recommendations that specify the required User-Wallet Instance interactions, as well as best design practices that may be followed to promote consistency across different Wallet Solutions in terms of how functionalities are accessed and used. 
 

Activation of the Wallet Instance 
**********************************

Activation is the essential step to enable the User to access the Wallet Solution's functionalities for securely obtaining, presenting, and managing their Electronic Attestations. The activation process involves User Authentication with the Wallet Instance using their digital identity, which enables the generation of the PID. 

Below are the functional requirements to support the User Experience related to the Activation of the Wallet Instance: 
- The User MUST download the Wallet Solution onto their device to generate their Wallet Instance; 
- The User MUST set up an unlocking method through a recognition mode (e.g., OTP, biometric authentication, Face ID, PIN). The User MUST use the selected recognition method each time they access the service to ensure security and protect their information; 
- The User MUST review all relevant information regarding the activation process and service usage. Additionally, the User MUST read any policy from the Provider and PID Provider and/or the service's terms and conditions. The User MUST give their consent to proceed or MAY decline to cancel the operation; 
- The User MUST select an Authentication option from those available; 
- The User MUST complete the Authentication flow with the Digital Identity Provider’s service; 
- The User MUST receive confirmation of the Authentication process outcome. If successful, the User MUST view a preview of their PID. The User MUST confirm the previewed information to proceed with Wallet Instance activation, or MAY cancel the operation; 
- The User MUST authorize the operation using the unlocking method previously set; 
- The User MUST receive confirmation of the successful activation of the Wallet Instance.

The User MUST always have the option to request the deactivation of their Wallet Instance, even in the absence of the device on which it was installed. For further details refer to the `Deactivation of the Wallet Instance <wallet-attestation.html>` section.

In case of errors, the User MUST receive consistent messages that inform them and guide them toward resolving the issue. For further details refer to the `Error Management <wallet-attestation.html>` section. 

For further details and resources refer to: www.wallet.gov.it. 

Issuance of Electronic Attestations of Attributes 
**************************************************

Once activation is complete, the User MAY obtain one or more Electronic Attestations of Attributes within their Wallet Instance. 

Depending on the User’s specific needs, the type of Electronic Attestation of Attributes, and the offerings available from the Wallet Provider, the Electronic Attestation of Attributes Provider, and the Authentic Source, the request of Electronic Attestations of Attributes can occur in two ways: 

- **From the Wallet Instance Catalog**: The User explores the list of Electronic Attestations of Attributes provided by the Wallet Solution, selects the one of interest, and initiates the request process, which concludes with obtaining the Electronic Attestation of Attributes in the Wallet Instance. 

- **From a Touchpoint of the Authentic Source** (or the Electronic Attestation of Attributes Provider if it coincides with the Authentic Source): The User interacts with the digital service of the Authentic Source, allowing them to obtain a specific Electronic Attestation of Attributes in their Wallet Instance via an Engagement Button.

Although the initiation methods for requesting the issuance may differ, the request flows share a similar structure and process. Below are the functional requirements to support the User Experience related to the request of an Electronic Attestation of Attributes from the Catalog: 

- The User MUST access their Wallet Instance using the previously set unlock method; 
- The User MUST select the Electronic Attestation of Attributes they wish to request from the available options in the Catalog; 
- The User MUST review certain minimum information before confirming the operation: PID data, if required by the Authentic Source for the request of the Electronic Attestation of Attributes, the name of the related Electronic Attestation of Attributes Provider, and any related information policy. The User MUST choose whether to disclose any additional non-mandatory data for the request (Selective Disclosure). The User MUST give their consent to proceed, or they MAY cancel the operation; 
- The User MUST view a preview of the Electronic Attestation of Attributes. The User MUST confirm the data shown in the preview to proceed with the request or MAY cancel the operation; 
- The User MUST authorize the operation using the unlock method previously set; 
- The User MUST view the positive outcome of the request; 
- The User MUST view the details of the requested Electronic Attestation of Attributes, including: the data contained in it, the name of the Electronic Attestation of Attributes Provider who issued the Attestation, and the name of the Authentic Source; 
- The User MUST have access to all issued Electronic Attestations by navigating the Catalog of the Wallet Instance. 

The User MUST always be able to request the revocation of the Electronic Attestation of Attributes, even without the device where the Instance was activated. For more details, refer to the `Management of Electronic Attestations <wallet-attestation.html>` section. 

In the event of communication issues between the systems of the Electronic Attestation of Attributes Provider and the Authentic Source, or if administrative or technical processes prevent the immediate issuance of the Electronic Attestation of Attributes, the request process MUST support deferred process. In this case:  
- Upon reaching the final step of the process, the User MUST be presented with a message prompting them to wait until the Electronic Attestation of Attributes can be issued. 
- The User MUST be notified by the Electronic Attestation of Attributes Provider once the Electronic Attestation of Attributes becomes available. 

If the User encounters incorrect data in an already obtained or in-progress Electronic Attestation of Attributes, they SHOULD receive appropriate assistance. For more information, refer to the `Assistance <wallet-attestation.html>` section. 

In case of errors, the User MUST receive clear, consistent messages that inform them and guide them toward resolution. For further details, refer to the `Error Management <wallet-attestation.html>` section. 

If an Authentic Source (or an Electronic Attestation of Attributes Provider, should it coincide with the Authentic Source) intends to implement an Engagement Button to initiate the request process from their Touchpoint, they MUST ensure compliance with the graphical appearance and implementation requirements for the Engagement Button, as outlined in the `IT-Wallet System Brand Identity <wallet-attestation.html>` section. 

Layout of Electronic Attestations 
==================================

The Electronic Attestations obtained within the Wallet Instance SHOULD be displayed in a list within a Preview View. In this case, the Electronic Attestations MUST ensure a high level of recognizability and accessibility [REF_ACCESSIBILITY] of the information contained. Below are the requirements for displaying the Electronic Attestation that each Wallet Provider MUST adhere to in order to provide a consistent and accessible consultation and usage experience: 

- The Electronic Attestation MUST be displayed correctly across all devices, ensuring a consistent experience on screens of varying sizes; 
- The name of the Electronic Attestation MUST be clearly visible and always displayed in both the Detail View and the Preview View; 
- The Electronic Attestation, in the Preview View, MUST display its validity status and MAY also include additional attributes to enhance the user experience and management; for example, it MAY display the name or logo of the Electronic Attestation of Attributes Provider or the PID Provider; 
- The layout of elements in the Preview View of the Electronic Attestation MUST be optimized for scalability and usability, especially when multiple Electronic Attestations are displayed on the same screen; 
- The Electronic Attestation MAY adopt a card format, in line with approaches already used by other Wallets in the market, to mirror the appearance of a corresponding physical document. When applicable, the digital nature of the document MAY be indicated, such as by labeling it as a "digital version" in the layout; 
- The Electronic Attestation MUST display the same information in the Detail View as shown in the Preview View and MAY include additional details; 
- The Electronic Attestation MUST include Action Buttons in the Detail View to allow for management, as outlined in the `Management of Electronic Attestations <Layout-of-Electronic-Attestations.html>` section. 

For further details and resources refer to: www.wallet.gov.it. 

Presentation of Electronic Attestations
****************************************

The presentation process allows the User to access a service or demonstrate ownership of certain data or their eligibility to perform a specific action. The presentation of Electronic Attestations and their subsequent verification involves interaction between two parties: the User and the Relying Party. This can take place in two main ways, depending on the circumstances and context of the interaction: 

- **Proximity Presentation**: The User presents the PID and/or a set of Attributes contained in one or more Electronic Attestations through the Wallet Instance, directly to a Verifier or to a Relying Party's device designated for in-person verification. 

- **Remote Presentation**: The User presents the PID and/or a set of Attributes contained in one or more Electronic Attestations through the Wallet Instance, to a Relying Party configured for online verification, for instance, to Authenticate and access the services offered. 


Proximity Presentation 
=======================

Proximity presentation allows the User to present the PID and/or a set of Attributes contained in one or more Electronic Attestations via their Wallet Instance, using one of two methods: 

- **Supervised mode**: The User presents the PID and/or a set of Attributes contained in one or more Electronic Attestations through the Wallet Instance to a Verifier equipped with a dedicated verification app or system (e.g., law enforcement officer, pharmacist); 

- **Unsupervised mode**: The User presents the PID and/or a set of Attributes contained in one or more Electronic Attestations through the Wallet Instance to a designated device (e.g., turnstile, ATM). 

Below are the functional requirements supporting the User Experience for both methods.

**Supervised Mode** 

- The User MUST access their Wallet Instance using the unlock method previously set; 
- The User MUST navigate to the feature dedicated to QR Code generation; 
- The User MUST present the generated QR Code to the Verifier acting on behalf of the Relying Party, who scans it using the designated verification app or system; 
- The User MUST review the requested PID data and/or Attributes, the name of the requesting Service Provider, and any related policy. The User MUST decide whether to share any non-mandatory PID data and/or Attributes (Selective Disclosure). The User MUST provide consent to proceed or MAY cancel the operation; 
- The User MUST authorize the operation using the unlock method previously set; 
- The User MUST receive confirmation of the successful presentation. 

If an error occurs, the User MUST receive clear and consistent messages informing them of the issue and guiding them toward resolution. For further details refer to the `Error Management`_ section. 

For further details and resources refer to: www.wallet.gov.it.  

**Unsupervised Mode** 

- The User MUST access their Wallet Instance using the unlock method previously set; 
- The User MUST navigate to the feature dedicated to QR Code generation; 
- The User MUST present the generated QR Code to the designated device (e.g., a turnstile) of the Relying Party for scanning; 
- The User MUST review the requested PID data and/or Attributes, the name of the requesting Relying Party, and any related policy. The User MUST decide whether to share any non-mandatory PID data and/or Attributes (Selective Disclosure). The User MUST provide consent to proceed or MAY cancel the operation; 
- The User MUST authorize the operation using the unlock method previously set; 
- The User MUST receive confirmation of the successful presentation. 

If an error occurs, the User MUST receive clear and consistent messages informing them of the issue and guiding them toward resolution. For further details refer to the `Error Management`_ section. 

For further details and resources refer to: www.wallet.gov.it. 

Remote Presentation 
====================

Remote presentation allows the User to present the PID and/or a set of Attributes contained in one or more Electronic Attestations by interacting with a Relying Party's Touchpoint through a designated Engagement Button. 

This presentation can occur in two different modes, depending on the type of device used to access the service: 

- **Same-device mode**: When the User accesses an online digital service using the same device on which the Wallet Instance is installed; 

- **Cross-device mode**: When the User accesses a digital service using a different device from the one where the Wallet Instance is installed. 

Below are the functional requirements supporting the User Experience for both modes. 

**Same-Device Mode** 

- The User MUST click the Engagement Button provided on the Relying Party's Touchpoint; 
- The User MUST access their Wallet Instance using the unlock method previously set; 
- The User MUST review the requested PID data and/or Attributes, the name of the requesting Relying Party, and any related policy. The User MUST decide whether to share any non-mandatory PID data and/or Attributes (Selective Disclosure). The User MUST provide consent to proceed or MAY cancel the operation; 
- The User MUST authorize the operation using the unlock method previously set; 
- The User MUST receive confirmation of the successful presentation within the Wallet Instance; 
- The User MUST return to the Relying Party's Touchpoint, where they MUST see confirmation of the completed presentation. 

If an error occurs, the User MUST receive clear and consistent messages informing them of the issue and guiding them toward resolution. For further details refer to the `Error Management`_ section. 

For further details and resources refer to: www.wallet.gov.it. 

**Cross-Device Mode** 

- The User MUST click the Engagement Button provided on the Touchpoint of the Relying Party while accessing the service from a different device than the one where the Wallet Instance is installed; 
- The User MUST access the desired Wallet Instance from the device where it is installed, using the unlock method previously set; 
- The User MUST scan the QR Code provided by the Relying Party using their Wallet Instance; 
- The User MUST review the requested PID data and/or Attributes, the name of the requesting Relying Party, and any related policy. The User MUST decide whether to share any non-mandatory personal data (Selective Disclosure). The User MUST provide consent to proceed or MAY cancel the operation. 
- The User MUST authorize the operation using the unlock method previously set; 
- The User MUST receive confirmation of the successful presentation within the Wallet Instance; 
- The User MUST return to the Relying Party's Touchpoint and MAY view confirmation of the completed presentation. 

If an error occurs, the User MUST receive clear and consistent messages informing them of the issue and guiding them toward resolution. For further details refer to the `Error Management`_ section. 

For further details and resources refer to: www.wallet.gov.it.

*Authentication* 

Authentication is a specific use case of remote presentation that allows the User to securely access services provided by both public and private Relying Parties. This is achieved by presenting the PID and, if necessary, a set of Attributes contained in the obtained Electronic Attestations of Attributes. This process ensures that the User retains control over their data, including the ability to share only the information strictly necessary for verification by Relying Parties. At the same time, it guarantees the reliability, authenticity, and validity of the data presented. 

The Authentication process can be carried out using both the same-device and cross-device modes described above. For the required User Experience functional requirements, refer to the functional requirements for remote presentation in same-device and cross-device modes. 

From a User Experience perspective, the Authentication process differs only in how it is initiated, which is through a dedicated Authentication Button. 

To ensure a consistent and seamless Authentication process across all Relying Parties, each Relying Party MUST adhere to the graphical and implementation requirements for the Authentication Button outlined in the `IT-Wallet System Brand Identity`_ section. Additionally, they SHOULD follow the relative technical requirements and use the open-source resources available at www.wallet.gov.it. 

Management of Electronic Attestations 
**************************************

The User must have the ability to manage their Electronic Attestations at any time. This section outlines three different categories of requirements for managing each Electronic Attestations, specifically regarding: 

- **Its status**: to allow the User to verify whether an Electronic Attestation is valid or invalid; 
- **Its usage**: to enable the User to view and manage the history of presentations carried out with an Electronic Attestation; 
- **Its data**: to allow the User to backup and restore each Electronic Attestation of Attributes in compliance with the principle of data portability. 

Below are the key aspects that impact and define the User Experience in managing Electronic Attestations, along with the functional requirements associated with each category. 

Status of Electronic Attestations 
==================================

To ensure reliability and promote the proper use of a Wallet Solution, the User MUST always have visibility of the status of the Electronic Attestations stored within their Wallet Instance, based on the information received from the Electronic Attestation Provider, which manages their lifecycle. 

Each Electronic Attestation can be either valid or invalid, with corresponding impacts on its usage opportunities: 

- **Valid**: Valid Electronic Attestations MUST be usable and therefore presentable. This category also includes Electronic Attestations that are nearing expiration. If an Electronic Attestation is about to expire, the User SHOULD be notified with adequate advance notice to allow sufficient time to request its reissuance or, if necessary, revoke it. 

- **Invalid**: Invalid Electronic Attestations MUST NOT be usable or presentable. This category includes expired or revoked Electronic Attestations. In such cases, the User MUST be informed of the invalid status and SHOULD receive the reason. If an Electronic Attestation is no longer valid and cannot be used in any scenario, the Wallet Solution MAY implement mechanisms to restrict access to the Detailed View of that Electronic Attestation. This is intended to encourage the User to update or delete the Electronic Attestation by providing appropriate informational text and a Call to Action. 

*Revocation of Electronic Attestations* 

Revocation is the procedure that turns an Electronic Attestation from a valid state to an invalid state. Revocation can occur in either an active or passive mode: 

- **Active revocation**: This refers to the revocation of an Electronic Attestation at the User’s request. This process affects only the Electronic Attestation and not its corresponding physical document, if one exists. Below is an illustrative list of scenarios in which the User MUST have the ability to request the revocation of an Electronic Attestation: 
	- The User decides they no longer wish to use a specific Electronic Attestation; 
	- The User decides to deactivate their Wallet Instance, thereby revoking all previously obtained Electronic Attestations; 
	- The User no longer has possession of the device on which their Wallet Instance is installed due to loss or theft. 

- **Passive revocation**: This refers to the revocation of an Electronic Attestation managed by the respective Electronic Attestation Provider on behalf of the Authentic Source. In this case, the User MUST be informed of the status change of the Electronic Attestation through their Wallet Instance and MAY additionally be notified via other Touchpoints managed by the Electronic Attestation Provider. Below is an illustrative list of scenarios that could lead to the revocation of an Electronic Attestation: 

	- The physical document corresponding to the Electronic Attestation has been reported lost or damaged by the User through the appropriate channel/ Touchpoint; 
	- The physical document corresponding to the Electronic Attestation has been revoked by the competent authorities; 
	- The minimum security and/ or reliability requirements for one or more involved parties are no longer met. 

For further details and resources refer to: www.wallet.gov.it. 

History of Electronic Attestations 
===================================

To ensure the principles of visibility and transparency, the User MUST be able to view the history of all presentations performed, in other words, the use of Electronic Attribute Attestations through their IT-Wallet Instance. In particular: 

- The User MUST see which Relying Party they have interacted with and which Electronic Attestations have been presented and verified; 
- The User MUST be able to easily request the Relying Party to delete their information related to previous presentations. 

For further details and resources refer to: www.wallet.gov.it. 
 
Backup and Restore of Electronic Attestation of Attributes 
===========================================================

With the aim of ensuring the principle of data portability, the User MUST have access to specific functionalities, particularly to: 

- Request the backup and storage of Electronic Attestations of Attributes obtained through their Wallet Instance; 
- Request the restore of their Electronic Attestations of Attributes on another Wallet Instance. 

For further details and resources refer to: www.wallet.gov.it. 

Deactivation of the Wallet Instance 
************************************

The deactivation of the Wallet Instance is the functionality that makes the Wallet Instance inactive and therefore no longer operational. The deactivation process can be triggered by different actors depending on the circumstances, specifically: 

- By the User, in cases such as: 
	- The device has been lost or stolen; 
	- The device has been compromised; 
	- The device has been reset to factory settings. 

- By an authorized third party, in cases such as: 
	- The Wallet Solution no longer meets the minimum security requirements. 

The User MUST have the ability to voluntarily deactivate their Wallet Instance through: 
- The Wallet Instance itself; 
- A Touchpoint (e.g., a website) provided by the Wallet Provider; 
- The device’s app store, by uninstalling the Wallet Instance. 

Below are the functional requirements to support the User Experience related to the deactivation of the Wallet Instance: 

- The User MUST access their Wallet Instance using the previously configured unlock method or MUST Authenticate at the Touchpoint provided by the Wallet Provider; 
- The User MUST select the Wallet Instance deactivation functionality; 
- The User MUST be informed that deactivating the Wallet Instance will invalidate previously obtained Electronic Attestations; 
- The User MUST confirm the action to proceed with deactivation, or MAY cancel the operation; 
- The User MUST receive confirmation of successful deactivation; 
- The User MUST be notified that the Wallet Instance is inactive when logging in again; 
- The User MUST have the ability to reactivate the Wallet Instance by re-downloading the app from the app store (if uninstalled) and/or by following the activation process again. For further details refer to the `Activation of the Wallet Instance`_ section. 

Once the Wallet Instance is reactivated, Electronic Attestations of Attributes can be re-obtained by starting the issuance or restore process again. For more details refer to the sections `Issuance of Electronic Attestations of Attributes`_ and `Backup and Restore of Electronic Attestations of Attributes`_. 

In case of errors, the User MUST receive clear and consistent messages that provide information and guidance for resolution. For more details, refer to the `Error Management`_ section. 

For further details and resources refer to: www.wallet.gov.it. 

Error Management 
*****************

The IT-Wallet System involves the interaction of multiple services provided by different actors. It is therefore important to define an effective error management model with the goal of improving the perception and reliability of the entire ecosystem and enabling the User to feel guided during interactions with the various Technical Solutions and to and to consciously manage any issues while using the service. 

Effective communication in case of an error also provides benefits for the actors involved, as it contributes to the reduction of assistance requests and, thus, to the minimisation of the impact on support systems. 

Below are the requirements and main best practices for error management, specifically related to the interaction between the User and their Wallet Instance. The User MUST receive timely and granular inputs from all Primary Actors involved in providing the service, each within their scope of responsibility, through their Wallet Instance. Each actor involved MUST, therefore, define a list of errors so as to ensure that the Wallet Provider can prepare an effective model for their management within the Wallet Solution considering the following dimensions and variables: 

- **The stage of the User Experience** where the error may occur: activation or deactivation of the Wallet Instance, obtaining, presenting, or managing Electronic Attestations of Attributes; 
- **The type of error**: system error, communication error between actors, etc.; 
- **The actor responsible** for the error: Wallet Provider, PID Provider, Electronic Attestations of Attributes Provider, Authentic Source; 
- **The way the error is displayed**: message on the page, banner, toast message, and so on; 
- **Suggested actions for the User** to resolve the error: suggestion to wait, request to try again, referral to FAQs and/or customer care, etc.; 
- **The method for error management**: opening an assistance request through the Wallet Instance, linking to other detailed channels, and so on. For further details, refer to the `Assistance`_ section. 

Below is a non-exhaustive list of the main error cases, with reference to the actor responsible for their management, for each phase of the User Experience. 

**Activation of the Wallet Instance**

.. list-table::
   :header-rows: 1

   * - Error type
     - Actor in charge
   * - The device does not support the Wallet Solution (e.g. absence of minimum security or technological requirements) 
     - Wallet Provider
   * - The Wallet Provider's services are unresponsive (e.g. technical errors or lack of connection) 
     - Wallet Provider 
   * - The PID Provider's services are unresponsive (e.g. technical errors) 
     - PID Provider
   * - The Authentication process on the Digital Identity Provider's service was unsuccessful (e.g. technical errors, unrecognized identity, etc.) 
     - Digital Identity Provider 

**Issuance of Electronic Attestations of Attributes **

.. list-table::
   :header-rows: 1

   * - Error type
     - Actor in charge
   * - The Wallet Instance and/or the PID are not active 
     - Wallet Provider 
   * - The service for obtaining an Electronic Attestation of Attributes is unavailable (e.g. technical errors) 
     - Electronic Attestations of Attributes Provider, Authentic Source 
   * - The User is unable to obtain a specific Electronic Attestation of Attributes in their Wallet Instance (e.g. no eligibility, invalid or expired physical version, etc.) 
     - Authentic Source 

**Presentation of Electronic Attestations** 

.. list-table::
   :header-rows: 1

   * - Error type 
     - Actor in charge 
   * - The User does not hold the required Attributes contained in one or more Electronic Attestations within their Wallet Instance to access a specific service 
     - Wallet Provider 

**Management of Electronic Attestations** 

.. list-table::
   :header-rows: 1

   * - Error type 
     - Actor in charge 
   * - The service for revocation/ backup/ restore of an Electronic Attestation of Attributes is unavailable (e.g. technical errors) 
     - Electronic Attestations of Attributes Provider 
   * - The service for revocation of PID is unavailable (e.g. technical errors) 
     - PID Provider 

**Deactivation of the Wallet Instance** 

.. list-table::
   :header-rows: 1

   * - Error type 
     - Actor in charge 
   * - The service for deactivating the Wallet Instance is unavailable (e.g. technical errors) 
     - Wallet Provider 

Assistance 
***********

For effective error management and the resolution of any other issues, the Primary Actors MUST ensure adequate support to the User by structuring a simple and effective assistance model. For this purpose, good practices are proposed on which such a model SHOULD be based: 

- **Self-resolution**: The User SHOULD be able to consult frequently asked questions (FAQs) about the content and functionalities of the Wallet Instance, in order to resolve any error cases or issues independently. 
- **Guided issue reporting**: The User SHOULD be guided through the process of opening an assistance request, in order to clearly define the issue and facilitate its resolution. 
- **Collaboration between actors**: Each actor involved (Wallet Provider, Electronic Attestations of Attributes Provider, PID Provider, and Authentic Source) SHOULD ensure the availability of dedicated back-office channels, configured according to their specific roles and operational procedures. The Wallet Provider SHOULD ensure that every request is directed to the appropriate actor in order to provide a prompt and accurate response, avoid overloading the actors involved, and improve the overall effectiveness of the assistance system. 
- **Efficient communication**: The User MAY track and MUST be updated on the status of their request throughout all stages of processing, with clear, continuous, and coordinated communication between all the actors involved. 

To implement these best practices, the Wallet Provider SHOULD establish a hierarchical assistance model: 

    1. **Level I | Self-management**: The User SHOULD have access to a Frequently Asked Questions (FAQ) section within their Wallet Instance to clarify doubts and resolve certain issues independently. Each actor SHOULD create specific FAQs and corresponding answers regarding the data and functionalities they provide. For certain error cases, the Wallet Provider MAY provide another actor's direct channel of support to facilitate a timely management and avoid opening an assistance request within the Wallet Instance. 
	2. **Level II | Requesting assistance** from the Wallet Provider: If Level I is insufficient, the User MAY open one or more assistance requests to the Wallet Provider. These requests SHOULD be managed through the Wallet Instance or other Wallet Provider Touchpoints. The Wallet Provider MUST diagnose and resolve the issue if it falls under their responsibility. 
	3. **Level III | Forwarding the request to the responsible actor**: If Level II is insufficient, the Wallet Provider SHOULD ensure that the request is forwarded to the responsible actor (Electronic Attestations of Attributes Provider, PID Provider, or Authentic Source), who MUST take charge of resolving the issue and communicate the outcome to the User. 

Here are the functional requirements supporting the User Experience related to Assistance: 

- The User MUST have access to assistance options at any point during the User Experience, with a clear indication of how to access them. 
- The User MAY open an assistance request through their Wallet Instance or other Touchpoints provided by the Wallet Provider. 
- When an assistance request is open, the User MUST receive prompt confirmation that the request has been acknowledged. 
- The User MUST be informed in advance if it is necessary to share their data with third parties. 
- The User SHOULD be informed when an assistance request needs to be managed outside of their Wallet Instance, such as on third-party channels. 
- The User CAN track the status of the request at any time through functionalities that MUST be made available by the actors dealing with the request. 

Feedback 
*********

User feedback collection allows for monitoring the User Experience, identifying potential areas for optimization, and continuously measuring the effectiveness of the service. Each Wallet Provider SHOULD establish a structured feedback collection system to monitor and improve the User Experience. 

This feedback system MAY be fed by two different types of feedback collection: 

- **Transactional Feedback** (Customer Effort Score, Customer Satisfaction): collected in response to specific actions, such as adding an Electronic Attestation or completing a presentation and verification process; 
- **Relational Feedback** (Net Promoter Score): not in connection with specific actions, collected to measure the overall perception of the User in terms of satisfaction, loyalty, and likelihood of recommending the service to third-party users. 

Here are some suggestions for implementing these types of feedback tools: 

**Transactional Feedback Collection** 

- **Customer Effort Score (CES)**: To measure the ease of use of the functionalities, surveys MAY be provided, for example, through components like modals or pop-ups within the Wallet Instance, triggered at the conclusion of specific actions or processes. Examples include: 
	- After completing the process of obtaining an Electronic Attestation; 
	- After the Authentication process, if positive; 
	- After the presentation process, particularly at the end of the first presentation opportunity and no more than once every 6 months; 
	- After the revocation and deactivation processes, to explore the reasons behind these actions. 
- **Customer Satisfaction Survey (CSAT)**: To measure the overall satisfaction of the User after a prolonged period of using the Wallet Instance, surveys MAY be provided, for example, through modals or pop-ups within the Wallet Instance. It is recommended to use the CSAT at intervals of no less than six months and as an alternative to CES, to avoid overwhelming Users with too frequent surveys. 

**Relational Feedback Collection** 

- **Net Promoter Score (NPS)**: To measure User loyalty and the likelihood of recommending the service to others, an evaluation MAY be requested from the User once or twice a year, either through the same service delivery channel (e.g. the Wallet Instance) or external channels such as email or SMS. This should be aligned with the overall feedback collection strategy.
