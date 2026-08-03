.. include:: ../common/common_definitions.rst
.. Included via infrastructure-trust.rst at title level '-' (level 1).

X.509 Certificate Profile
-------------------------

This section defines a general **X.509 Certificate Profile**, which is further specialized for the following artifacts:

- :ref:`infrastructure-trust:Entity Sign/Seal Certificate Profile` (EUDIW and National Trust Framework);
- :ref:`infrastructure-trust:Trust Anchor Certificate Profile` (EUDIW and National Trust Framework);
- :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile` (EUDIW Trust Framework);
- :ref:`infrastructure-trust:Registrar Sign/Seal Certificate Profile` (EUDIW Trust Framework).

The common profile establishes the syntax, semantics and encoding requirements for X.509 certificates based on :rfc:`5280` and ETSI EN 319 412.
Each X.509 certificate profile defined by this specification MUST conform to the requirements of this section unless explicitly stated otherwise.

The final certificate is obtained by combining the certificate body (``version`` through ``subjectPublicKeyInfo``) with the certificate extensions required by the selected certificate profile.
The resulting ASN.1 structure MUST be encoded using the Distinguished Encoding Rules (DER) as specified in :rfc:`5280`.

Common Certificate Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

The ``TBSCertificate`` structure and its fields MUST conform to :rfc:`5280#section-4.1`.

The following table defines the certificate fields applicable to the certificate profiles defined in this specification.
For each field, the table specifies the corresponding :rfc:`5280` reference, its presence requirement, and any additional profile-specific constraints.

.. list-table:: Certificate Profile Fields
   :class: longtable
   :header-rows: 1
   :widths: 20 60 20

   * - **Field**
     - **Description**
     - **Reference**

   * - ``version``
     - REQUIRED. It MUST be version 3 (value ``2``).
     - Section 4.1.2.1

   * - ``serialNumber``
     - REQUIRED.
     - Section 4.1.2.2

   * - ``signature``
     - REQUIRED. The referenced algorithm MUST be among those defined in :ref:`algorithms:Cryptographic Algorithms`.
     - Section 4.1.2.3, Section 4.1.1.2

   * - ``issuer``
     - REQUIRED. It MUST comply with the applicable requirements of [`ETSI EN 319 412-2`_] (Clause 4.2.3.1 for **legal persons**, Clause 4.2.3.2 for **natural persons**), as specified by the corresponding certificate profile.
     - Section 4.1.2.4

   * - ``validity``
     - REQUIRED.
     - Section 4.1.2.5

   * - ``subject``
     - REQUIRED. It MUST comply with the applicable requirements of [`ETSI EN 319 412-2`_] (Clause 4.2.4) for **natural persons** and [`ETSI EN 319 412-3`_] (Clause 4.2.1) for **legal persons**, as specified by the corresponding certificate profile.
     - Section 4.1.2.6

   * - ``subjectPublicKeyInfo``
     - REQUIRED. The referenced algorithm MUST be among those defined in :ref:`algorithms:Cryptographic Algorithms`.
     - Section 4.1.2.7

   * - ``issuerUniqueID``
     - OPTIONAL. It SHOULD NOT be present.
     - Section 4.1.2.8

   * - ``subjectUniqueID``
     - OPTIONAL. It SHOULD NOT be present.
     - Section 4.1.2.8

   * - ``extensions``
     - REQUIRED. It MUST conform to the structure defined in :rfc:`5280#section-4.2`.
       The applicable extensions and their profile-specific constraints are defined in :ref:`infrastructure-trust:Supported Certificate Extensions` and in the corresponding certificate profile.
     - Section 4.1.2.9

Supported Certificate Extensions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table lists the certificate extensions supported by the X.509 certificate profiles defined in this specification, together with their object identifiers, default criticality, and normative references.
Specific certificate profiles define whether an extension is REQUIRED, OPTIONAL, or MUST NOT be present, and MAY further constrain its contents.

The criticality values used in this specification have the following meaning:

- **C**: the extension MUST be marked critical;
- **NC**: the extension MUST be marked non-critical.

.. list-table:: Supported Certificate Extensions
   :class: longtable
   :header-rows: 1
   :widths: 25 20 15 40

   * - **Extension**
     - **OID**
     - **Criticality**
     - **Reference**

   * - ``authorityKeyIdentifier``
     - ``2.5.29.35``
     - NC
     - :rfc:`5280#section-4.2.1.1`, Clause 4.3.1 of [`ETSI EN 319 412-2`_]

   * - ``subjectKeyIdentifier``
     - ``2.5.29.14``
     - NC
     - :rfc:`5280#section-4.2.1.2`

   * - ``keyUsage``
     - ``2.5.29.15``
     - C
     - :rfc:`5280#section-4.2.1.3`, Clause 4.3.2 of [`ETSI EN 319 412-2`_], Clause 4.3.1 of [`ETSI EN 319 412-3`_]

   * - ``certificatePolicies``
     - ``2.5.29.32``
     - NC
     - :rfc:`5280#section-4.2.1.4`, Clause 4.3.3 of [`ETSI EN 319 412-2`_]

   * - ``subjectAltName``
     - ``2.5.29.17``
     - NC
     - :rfc:`5280#section-4.2.1.6`, Clause 4.3.5 of [`ETSI EN 319 412-2`_], Clause 6.6.1, GEN-6.6.1-07 of [`ETSI TS 119 411-8`_]

   * - ``basicConstraints``
     - ``2.5.29.19``
     - C
     - :rfc:`5280#section-4.2.1.9`

   * - ``cRLDistributionPoints``
     - ``2.5.29.31``
     - NC
     - :rfc:`5280#section-4.2.1.13`, Clause 4.3.11 of [`ETSI EN 319 412-2`_]

   * - ``authorityInfoAccess``
     - ``1.3.6.1.5.5.7.1.1``
     - NC
     - :rfc:`5280#section-4.2.2.1`, Clause 4.4.1 of [`ETSI EN 319 412-2`_]

   * - ``ext-etsi-valassured-ST-certs``
     - ``0.4.0.194121.2.1``
     - NC
     - Clause 5.2.2 of [`ETSI EN 319 412-1`_]

   * - ``noRevAvail``
     - ``2.5.29.56``
     - NC
     - :rfc:`9608#section-2`

   * - ``qcStatements``
     - ``1.3.6.1.5.5.7.1.3``
     - NC
     - :rfc:`3739#section-3.2.6`, Clause 4.2 of [`ETSI EN 319 412-5`_]
