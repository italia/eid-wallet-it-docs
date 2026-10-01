.. include:: ../common/common_definitions.rst
.. Included via wallet-instance-functionalities.rst at title level '=' (document title).


User's Attributes Deletion
==========================

This Wallet Instance functionality allows Users to obtain a list of all Relying Parties towards which Digital Credentials have been presented. Users may then request deletion of the attributes of one or more Digital Credentials presented to a Relying Party of their choice. The request uses the common interface of `EUDI-TS 7`_. The high level flow is presented below (:ref:`WP_115 <user-attribute-deletion-testcases>`).

.. plantuml:: plantuml/user-deletion-attribute-flow.puml
    :width: 99%
    :alt: The figure illustrates the Deletion of User's Attributes Process.
    :caption: Deletion of User's Attributes Process.

**Step 1:** The User requests the deletion of attributes by invoking the Wallet Instance's attribute deletion function.

**Step 2:** The Wallet Instance collects all transaction data and shows the User the list of Relying Parties with which it has had interactions throughout the Wallet Instance lifecycle and that are in possession of the User's attributes (:ref:`WP_115a <user-attribute-deletion-testcases>`).

**Step 3:** The User selects the target Relying Party for attributes deletion.

**Steps 4 - 5:** The Wallet Instance determines the contact channels registered for that Relying Party (:ref:`WP_116 <user-attribute-deletion-testcases>`).

In the National Trust Framework, the contact is the ``support_uri`` of the registration Trust Mark, as defined in :ref:`infrastructure-trust:Trust Mark Types and Schema`.

In the EUDIW Trust Framework, the contacts are the helpdesk and support values in the Subject Alternative Name of the Wallet-Relying Party Access Certificate, as specified in `EUDI-TS 7`_.

**Step 6:** The Wallet Instance logs the initiation of the data deletion request as defined in :ref:`wallet-instance-dashboard:Wallet Instance Dashboard and Transaction Logging`. These logs MUST include at least (:ref:`WP_117a <user-attribute-deletion-testcases>`):

  * the date and time of the request,
  * the Relying Party to which the request was made,
  * the attributes requested to be removed.

**Steps 7 - 8:** The Wallet Instance MUST display the contacts that the platform can invoke, or apply a previously configured User preference. It MUST then invoke the external application that corresponds to the selected contact (:ref:`WP_117 <user-attribute-deletion-testcases>`, :ref:`WP_118 <user-attribute-deletion-testcases>`).

- The Wallet Instance MUST open an HTTPS URL in an external browser.
- The Wallet Instance MUST open an email address in an external mail client, when a mail client is available, as a ``mailto`` URI. The ``subject`` MUST state that the User requests the erasure of personal data pursuant to Article 17 of Regulation (EU) 2016/679 previously provided through the Wallet Instance. The ``body`` SHOULD identify the attributes requested for erasure, or state that all personal data previously provided through the Wallet Instance are requested for erasure.
- The Wallet Instance MUST open a telephone number in the phone application, when a phone application is available.

**Step 9:** Before deleting the attributes, the Relying Party MUST authenticate the User, or the request, with an authentication mechanism of its choice. The Relying Party SHOULD use the authentication and signature facilities of the User's Wallet Instance. Upon authenticating the User, the Relying Party MUST delete the attributes of the Digital Credentials identified by identity matching, as specified in :ref:`identity-matching`.

.. note::
  The specific authentication mechanism is left to the Relying Party. If the User does not authenticate through the Wallet Instance, identity matching and identity reconciliation MAY use a preexisting national authentication scheme, where possible, as specified in :ref:`identity-matching`. Upon authenticating the User, the Relying Party MAY prompt the User to confirm the deletion.

**Step 10:** The Wallet Instance MUST inform the User that the data deletion request has been initiated (:ref:`WP_119 <user-attribute-deletion-testcases>`, :ref:`WP_119a <user-attribute-deletion-testcases>`). The completion of the deletion by the Relying Party is outside this protocol, as specified in `EUDI-TS 7`_.
