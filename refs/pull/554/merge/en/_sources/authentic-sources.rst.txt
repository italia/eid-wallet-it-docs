.. include:: ../common/common_definitions.rst


Authentic Sources
+++++++++++++++++++

Authentic Sources are responsible for the authenticity of the User's attributes provided as Digital Credentials by Credential Issuers. During the Issuance Flow, Credential Issuers request from Authentic Sources the attributes required to provide the requested Credential. Authentic Sources MAY also provide a Credential Offer related to their Credential Issuers as defined in Section :ref:`Credential Offer Endpoint <Credential Offer Endpoint>`.

    - The Authentic Source MUST provide an e-service registered within the PDND catalogue which the PID/(Q)EAA Provider, as the recipient, MUST use to request the User's attributes.
    - In case of unavailability of the User's attributes, the Authentic Source MUST provide a response to the PID/(Q)EAA Provider with an estimation time when a new request can be sent. 
    - The PID/(Q)EAA Provider MUST provide to the Authentic Source an evidence that:
    
        - the request for Users attributes is related to data about themselves;
        - the request for User attributes comes from a valid Wallet Instance. 

    - The PID/(Q)EAA Provider MUST make available to the Authentic Source an e-service for notifications on attributes availability and validity status (revocation or updates). The Authentic Source MUST use this e-service to notify to the PID/(Q)EAA Provider the notifications on the availability of the User's attributes as well as those relating to the attributes updates. 
    - The protocol flow MUST ensure integrity, authenticity, and non-repudiation of the exchanged data between the Authentic Source and the PID/(Q)EAA Provider. 
    - The e-services MUST be implemented in REST. SOAP protocol MUST NOT be used.

.. note::
  
  In case of the PID/(Q)EAA Provider and the Authentic Source are separate entities, the Authentic Source MAY provide a Credential Offer related to its PID/(Q)EAA Provider as defined in the Section :ref:`Credential Offer`.


Security Patterns
----------------------

Authentic Sources MUST:

    - provide User's attributes when requested by the Credential Issuer authorized to issue the related Digital Credential attesting the attributes. Public Authentic Sources MUST use PDND to send User's attributes to their Credential Issuers. When the User's attributes is not available duting the Issuance Flow, Authentic Sources MUST provide Credential Issuers with an estimated time when the User's data will be available. Authentic Sources MAY require an evidence that: 
        
        - the request for Users attributes is related to data about themselves;
        - the request for User attributes comes from a valid Wallet Instance;

    - cooperate with their Credential Issuers so that the attributes attested in a Digital Credential are always kept up to date. Public Authentic Sources MUST use PDND to notify their Credential Issuers of any update regarding attributes that have changed or are no longer valid. 


