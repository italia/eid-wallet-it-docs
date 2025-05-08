.. include:: ../common/common_definitions.rst

Credential Issuance High-Level Flows
=======================================

High-Level PID flow
-------------------

The :numref:`fig_High-Level-Flow-ITWallet-PID-Issuance` shows a general architecture and highlights the main operations involved in the issuance of a PID.

.. _fig_High-Level-Flow-ITWallet-PID-Issuance:
.. figure:: ../../images/High-Level-Flow-ITWallet-PID-Issuance.svg
    :figwidth: 90%
    :align: center
    :target: https://www.plantuml.com/plantuml/svg/nLLjRzf84FxEhzYYI2LIgA6GbrP9L0gaiKHY1AHHfKZMUdTYLZ6xljqr2NUw_twpTWmaXShV3Y7PEpFxp3ClC_vcBDKsMoIr3qAo9ED0vjQcvgldQVhyAHPsdaMP0SsKj23j9wOMNffGwUuqZUM9YBn-jpbsehkRaRUWne96KTXNYrH9ToTr-DV-O1XEPyF9C9Zz6WyRXxLHxrTmDmj7mwjPEF5_NCzGzf6yIcV1E1m4zxSegvad8LEgwO8aGe9TfK2KjdErhP6AWu6Kj5kjBQccyYcNdhPgY3s0HmGWq_74dmsdjG-yEFVzeJ-ucumgX2uiJGJrc81ch6aw5ynudQZJvUtEMHTEZwEpzbatYavE7rkjgFtvosdhv95zwV0M7BUzwSyV7W9f6Y9aY1YVp39Ui_3xmMqr4ZPBATUTJHq4QfkFQD4qgHOMp6iPogAkmJsylb0ohyZloXo1FeDH2sWUUmoq5O-2KGlLBd1gQKHDHUj4iQTgbYv-Kv6pYYjQ8kOIT3NR9rXLPrhDKl2GKSsh6SCBcrCPGqWJMx4KO9wiIgiPFzCaWIh0df362fjPKVPGhSVv198PZHjrQbQIrO_8WOKNsrU9qXS7lSaak0-lWjjPs0z6mGIrReQtjMyKKxjAu690pHpu2C-DGvp_CMYZPCCbzuZKx_1Hn-TzpfhuI8bA1cIk4ewQmwr1DojZOK4YbKbEzGeLtrzV6qNCKvNamMpWIadzaFnJ8_ZxI6wea8ILsypaqlLoQpoBtxauUe4_wFxi--wrVdHGpEL5lN1RaFotLblJIGKVQxKKF0znx0z8UQnCPCaS4tIvaPdzH5xx3vcyHT4fsc55LqB6P4orNMsKhsXzuf5fxsRq3j6D7i9XL9kmV8xNX5rjnORBLd0o4B5RfQGqU93a2j20lilz_xAHdUjftZhXyCKs17SvAPbk2eF2zs4Gm-Qm0EAs82TAaYBQaUgHQn7FIMFKESHxcofivgb8tJhNkMTgq4SlitE7ph0tCrqqL-zsF7cN_dBv8ivR44lHS9DSCWMz50mCeN9JXxw6F0IQ6DAdA55nLhPnyseu81fYOQnUlVFgbhZhvXgsJ36WE0_rSoF-Xg_jayjpvWQT8FZbUNJPElUYotClb-7J6Lq-o7igBP8XsFJrepg2EIX4iNGlK7idqFRKO626gILex2mNvqndnhw1NxBzH3_ln9_0NnaOQzuoHPm_KUtiX2hsnGwsP0TP74bimRqUkZizhBk6MZ0F4W-aM9mErS66TpbrQlO27-y43Y9BiMtHWxLQH1d25w3VHPaEdQB0_GyiZSr5yM5mRak3F_J8oKwdlZ4PR2N-6qYEdv__0000

    PID Issuance - General architecture and high level flow.

The high-level flow begins with the User who wants to obtain a PID and starts his/her Wallet Instance (Step 0). Below the description of the steps represented in the previous picture:

    1. **PID Provider Discovery and Trust**: the Wallet Instance discovers the trusted PID Provider using the Digital Credential Catalogue and Federation Services, establishing the trust to the PID Provider according to the Trust Model and obtaining its metadata that discloses the formats of the PID, the algorithms supported, and any other parameter required for interoperability needs.
    2. **PID Request**: using the Authorization Code Flow defined in [`OpenID4VCI`_] the Wallet Instance requests the PID to the PID Provider.
    3. **Wallet Provider Discovery and Trust**: the PID Provider checks the authenticity and validity of the Wallet Instance, establishing the trust to the Wallet Provider and obtaining Wallet metadata with the parameters required for interoperability needs, according to the Trust Model.
    4. **User Authentication**: the PID Provider authenticates the User with CieID LoA High (L3), acting as an Identity and Access Management Proxy to the National eID system.
    5. **Fetch of PID data from National Public Registry**: the PID Provider obtains the required PID data from National Public Registry (ANPR) which acts as Authentic Source.
    6. **PID Issuance**: the PID Provider releases a PID bound to the key material held by the requesting Wallet Instance.


High-Level (Q)EAA flow
----------------------

The :numref:`fig_High-Level-Flow-ITWallet-QEAA-Issuance` shows a general architecture and highlights the main operations involved in the issuance of a (Q)EAA, following the assumptions listed below:

  - the User has a valid PID stored in their own Wallet Instance;
  - the (Q)EAA requires a high security implementation profile.

.. _fig_High-Level-Flow-ITWallet-QEAA-Issuance:
.. figure:: ../../images/High-Level-Flow-ITWallet-QEAA-Issuance.svg
    :figwidth: 90%
    :align: center
    :target: https://www.plantuml.com/plantuml/svg/ZPJ_Rzgy4yT_pr_XeKgZKccWq2-TsceCw8R46Zv0LqsQ55tYQx0QxCnsQFayUlxtvqo0jfHMYP12xiwlUv_Flg_6WhRvBFK-2HcdEKSsjJOpNtnVm-DX8kmqZtA3EbRIehI7iPhvMGhIhQaPorCH-PrMRUXCjpy7_WoCHKsciADccP9kJURuF_hTNZYUz4QzOF9xsAlkUuFsx-1s4WvwrvDmrF_-OqAspsnbdGJ3i1lStP3DCmz2Pg1Xnb8XqIuoP4hRgV8yzkoIYgF1Z3NgzPTc3VB1cO-QvnxHktXF23OUZlgJtjZxn8llJh_NxzwE1YMA5nPI0Nuii9PeoAOYDdupQhPuetdMmjFZwAnnregYazFxUZrg79sVra_ku_Cch-Dnmn__-kuJI4D8o90OXsQUR5JqEy5DEH4spu3hvdCd17bhznHHCvaM5isg4Pkshk4-BPyfMVJaZND9W4SqQeQrOpz6RSMzYC5YkGKSB4HWIaQdAdue5-dgDoKrgwHa937dgCl5Fk2YhDAoIC7363Gl5unFyHHaWY6ajcGhq3nObPKBVeGqnJ9WNqXZXSsjM9yXhytv2DC99DKAc8MCAmTip-AJxQXKwSkzzcWKt8NNmSqax0I3O4HUTujVULywndQHucKNp1JvWBwh-pG1XgYDabMtkGUiSakl2htlbgfPdoI1Z95DLSh9i__Yefk5iJXZaSeb1xqWnxVLtsfHyrYbosAUSMjBPP_zup5wFhEV82IBr_FCBAsRyLPz56-rE7b1lzlwrUapdot_3PsjSh1NND3BIf6_KFklvsrq_KM0eLPpmPV5Ll-ttsktsTfIMjKyTh8e_xFDl52r9MPr64dDQuhEA8xQkn0oOKFGTl7iT8YTbRahI2GgYfvDUDXxibKm5DhExPGC8gQzpdMnMLk8zI0Xp6k01GgyHeuQN9FO6FLSn6WOICww8d7ZcNKqSfS0KiCwG1QLvEkMrAvxNQOn4SRgnLPMDv0e8prKSd7QgBcL2oF-ZryQ9rSNiJkrZEXN5z5L_SAFhYxyfOtUBkZgZxm3QKaDA_fMEQWGqD48PE5TLcCdQwltL9-9rHpruezqvKvqRkoh3FFuVRb7ErECy6-EnXfAjYMOM1yfRkx45TTWXsBsLd1uIyVhemrkxKonEJrWaMJJ1tC3eS2kk4uxc7V1npl1GMH1I4CPhDKYoWbVGB-9zNxeZ0pkjsSXCPUhWKTfrm4VL7EoCsdVc1otTlyhIawZzJy0

    (Q)EAA Issuance - General architecture and high level flow

Similarly to the PID high-level flow, the above diagram depicts a (Q)EAA high-level flow starting from the User who wants to obtain a (Q)EAA (step 0). Below the description of the most relevant operations involved in the (Q)EAA issuance:
    1. **(Q)EAA Provider Discovery and Trust**: the Wallet Instance obtains the list of the trusted (Q)EAA Providers using the Digital Credential Catalogue and Federation API (e.g.: using the Subordinate Listing Endpoint of the Trust Anchor and its Intermediates), then inspects the metadata looking for the Digital Credential capabilities of each (Q)EAA Provider.
    2. **(Q)EAA Request**: using the Authorization Code Flow, defined in [`OpenID4VCI`_], the Wallet Instance requests a (Q)EAA to the (Q)EAA Provider.
    3. **Wallet Provider Discovery and Trust**: the (Q)EAA Provider verifies the authenticity and validity of the Wallet Instance. During this step the (Q)EAA Provider establishes trust with the Wallet Provider and retrieves Wallet metadata containing the necessary parameters for interoperability, as defined by the Trust Model.
    4. **User Authentication**: the (Q)EAA Provider, acting as a Relying Party Instance, authenticates the User evaluating the presentation of the PID.
    5. **Obtaining Attributes**: the (Q)EAA Provider fetches User attributes from the relevant Authentic Source.
    6. **(Q)EAA Issuance**: the (Q)EAA Provider releases a (Q)EAA bound to the key material held by the requesting Wallet Instance.

