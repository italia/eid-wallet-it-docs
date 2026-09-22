.. include:: ../common/common_definitions.rst
.. Included via credential-issuance.rst at title level '=' (document title).


Credential Issuance High-Level Flows
=======================================

High-Level PID flow
-------------------

This flow applies after the condition in :ref:`pid-until-notification`.
Until then, the High-Level IT-Wallet ID flow applies.

The :numref:`fig_High-Level-Flow-ITWallet-PID-Issuance` shows a general architecture and highlights the main operations involved in the issuance of a PID.

.. _fig_High-Level-Flow-ITWallet-PID-Issuance:

.. plantuml:: plantuml/pid-issuance-high-level-flow.puml
    :width: 99%
    :alt: The figure illustrates the general architecture and high level flow for PID issuance.
    :caption: `PID Issuance - General architecture and high level flow. <https://www.plantuml.com/plantuml/svg/ZLPXQ-Cu4FtkNp5d2fT2UscltJrOqh1P9xqQiflWf5SM2aQrfuwe8_caSLhlSV_zHlOsSNlfhaD0zcZqtjFeZV17Iy9GkSxXIcQhuobkC8TvE8RGsbAe1E4oru_UBr8bUPaY38BpVd0U1rgHa0hDqFEkml4aNYmdqMIs_3gVz0wzwUZhx7ePJoUNopWA_xnQSiop3r8LmeWrvBoGgW916rhfreJIALeiuFJaf1KrGZtKqJzEFEzN6ECzhuV5F0gNaqLB6PM5ICrPFz7hjLR3FJFthFfOFABLQpn-rq_GaBoNYI3ia9qA4dV2TadDTVBG8QsqQ6mNdJhhaiPe6pGT4X-mwgYkGvfCuqIOj4CcFYKheJACHKvTwetsWNJH8VDHv3d-5B8lbIL99Kbd3c-KfX7cIv7rV64hbVX7S43uH87EjRau64NHx2Q-d7rPni5iEejurjcsFVjYOa5LZXTZOLUOJlczTyYMdwEnMlLS9O_0l-R1v_6cbWiXowaRRANpb6SElMrJzHxb__FSqbauFlyh2A4FzTFSnS0fjuMHX1T-Kmh6-gHBbGfJzGgPpetUoBJMu3gxUNMCy8y7_DlnRX97p0mSMnTQeIBRudMF_j6MxFlHCzjB55Dm7XUtaYg3kJ1KxU2-emMyXSNey_GLedCwm_sxan-cl4XIrTf344va2cEPIH8vF2VSAhX4JX3kVBTRMrIMS1rFdgWdKoVhENrN1Gw-nWARh72DuDez1QsWePpgKNrBGczwTjYkUijPJltk86jYOPbYLDBAWIUmqALfJdFqPHwzAi3p9SCmBq58SEBaUXpUmDAKbc31tIuJj23KhXY1mNeB8hSG28xepD-kYp2JbaprYj9TLapdyO4rJcNp-GChl-67q_V3GU8S3umx7DmDJmRzk-6WNyTuT4d3MtKZ5B4EO7FvHpvZEIX68V4cqEbUeBOxUKysqHiqVBAynMRNB-0toTj2Vz-B7-7V9LgoBvKope-adks5QffpZrhO8vORWjtt9iFvNeQjOmIXlLNy0ku6sQB6rxLoOT_4VRSNTtRdR6MPWCZ8kvBH6ynFyhaQfk20-n-GoEn5Sq7kglKZXxpVo-a-9h1LTgK9mN0h4UXxU9HUuscBEIQkYq3GxWCaMMbjUNNZuaBGwWFSHFDHS2nQ9Kh1oapnK7CP-8maN3VLvz4iTHNLHduJZk8tpqEUSKgyZ_nKhlF_0000>`_

The high-level flow begins with the User who wants to obtain a PID and starts his/her Wallet Instance (Step 0). Below the description of the steps represented in the previous picture:

    1. **PID Provider Discovery and Trust**: the Wallet Unit discovers the trusted PID Provider using the Digital Credential Catalogue and selects exactly one path according to :ref:`trust-evaluation:Selection at Issuance`. The EUDIW path authenticates the access-certificate-signed Issuer Metadata and uses EUDIW Authorization (:ref:`trust-evaluation:EUDIW Authentication`, :ref:`trust-evaluation:EUDIW Authorization`, and :ref:`trust-evaluation:EUDIW Metadata Retrieval and Validation`); on the National path, the Wallet Unit MUST evaluate trust using the Federation Entity Authentication and National Authorization (:ref:`trust-evaluation:Federation Entity Authentication` and :ref:`trust-evaluation:Authorization`) and MUST obtain the applicable final metadata through :ref:`trust-evaluation:Metadata Retrieval and Validation`. The Wallet Unit obtains metadata that discloses the formats of the PID, the algorithms supported and other interoperability parameters (:ref:`WP_045–046 <wallet-credential-issuance-testcases>`). A failed path MUST NOT be retried with the other path.
    2. **PID Request**: the Wallet Unit requests the PID using the Authorization Code Grant supported by the PID Provider (:ref:`WP_051 <wallet-credential-issuance-testcases>`).
    3. **Wallet Provider Discovery and Trust**: the PID Provider checks the authenticity and validity of the Wallet Instance, establishing the trust to the Wallet Provider and obtaining Wallet metadata with the parameters required for interoperability needs, according to the Trust Model.
    4. **User Authentication**: the PID Provider authenticates the User using National CieID LoA High (L3).
    5. **Fetch of PID data from National Public Registry**: the PID Provider obtains the required PID data from National Public Registry (ANPR) which acts as Authentic Source.
    6. **PID Issuance**: the PID Provider releases a PID bound to the key material held by the requesting Wallet Instance.

High-Level IT-Wallet ID flow
----------------------------

The :numref:`fig_High-Level-Flow-ITWallet-ID-Issuance` shows a general architecture and highlights the main operations involved in the issuance of an IT-Wallet ID.

.. _fig_High-Level-Flow-ITWallet-ID-Issuance:

.. plantuml:: plantuml/it-wallet-id-issuance-high-level-flow.puml
    :width: 99%
    :alt: The figure illustrates the general architecture and high level flow for IT-Wallet ID issuance.
    :caption: `IT-Wallet ID Issuance - General architecture and high level flow. <https://www.plantuml.com/plantuml/svg/ZLP_Rzf84FtVds8ELJeY9KToINjIHL2f8HSa6X0uZIeXMOizmQkONMvtJEAUxhlVh0dOKDAQVsplpButFzwC-6H96CgMATpAHN8sn3McC0ZE7aIQ8i6W1mDhCw4YX9jKFtk_IHMbMOpGzgzQ_bNeQqL2AZGTpxiTzFhXDEXF-gFWsxZVFF66tM-Z-o0Szc-2S3Bu-pRWCyy-IRKIHYmXvOkKhn2qeKHN34h7Q7455-VdbLCZr5Dn-jUvv_qEFNpa-p0TJmP1Vrg9ZBALYCrbAzBBfLQT8vP7ZlfCFAFLIpnxtuhGa7oKaI2iuHqB4dDXwxYcEdgguPPPDBPEd7fHnutHrcXgE3vXNZEw6cuo3YDXuXgU-18bGYqm52dLgJVQ9zAh6fxFJhI_X6n9PKbIHjA9m-l6yGJJG2oQ3M5p5JLEuHtX2_awrURwNNSo6Js4DwEx8FH7mz64hKwsUzQgOKfvYjSzOHECX_pTF679Zz5OhPgkagVGkET7Wv_R6UDmYW5BT1gpvSJR3LNpMVxevwwE1hshh_x0lO8BsAwC9BnkR2h049zrfc9XyYOACJPwBUE2Uc-o-zqk5BQ25VxrW7ybzpfovCp2PykLLgZ87d0tJdVCh-rdwdqKis8_Bd0krGB6mb1UmhsY-T22QVVBy03HgPtX_Yjp6SHyIL9UISWVz6KCFRcG95BOEimKt20x2DVZNMhJt18km_uBDMNimjgwbrNWmqCii562ImGtyZ5e1HlAeUuMAnEQmyiJq0QGAphDvgv79Fb-DwF48KH54F0iAO4law07Nz78nzVZQkygidHfboee8XQMOzjXmbHdPYE5xjruSb2vxOPYc7qG4knuLp1pX879BC4KpLf6Q46eif2-mHYBF2puWa_q8iD6zRB1XRHayWDgj_6OrkEER-JE2cwqhVoE7oy-TDgH6njWy4vxtZblj-QTTgiuuwTpwipKWr34mS1CLSNQE6qmh4DbG19lObuSnQmYpLHLzvonZVGQ3Ml65M2_E7kiw-ZjLFuyIZl1VpAqP66VttLH6_bz8mnVnrZoCCdFqhiyohF1BdEQgLrMhgk7kV18ilxVvBWwob6HCzgPuWzmUso76juNiGlx9kxxexYZkTEdPG8Y8-SPesymFyjjFJXUbfXJ6Oc5lTwiwR9UFvFOX-Doi3P32p_gIsb2C3pL1FgHHzRRZ8Z55AEYMOBA_qDHehL5Mqfc9IZvM5ayq2yMoE4cs9FPdXR-y3naeul2-yHlsJBr_WS0>`_

The high-level flow begins with the User who wants to obtain a IT-Wallet ID and starts his/her Wallet Instance (Step 0). Below the description of the steps represented in the previous picture:

    1. **IT-Wallet ID Provider Discovery and Trust**: the Wallet Unit discovers the trusted IT-Wallet ID EAA Provider using the Digital Credential Catalogue and selects the National path for this national-only Credential. The Wallet Unit MUST evaluate trust using the Federation Entity Authentication and National Authorization (:ref:`trust-evaluation:Federation Entity Authentication` and :ref:`trust-evaluation:Authorization`) and MUST obtain the applicable final metadata through :ref:`trust-evaluation:Metadata Retrieval and Validation`; no EUDIW evidence is added as a supplement or fallback. The metadata discloses the formats of the IT-Wallet ID, the algorithms supported, and other interoperability parameters (:ref:`WP_045-046 <wallet-credential-issuance-testcases>`).
    2. **IT-Wallet ID Request**: the Wallet Unit requests the IT-Wallet ID using the Authorization Code Grant(:ref:`WP_051 <wallet-credential-issuance-testcases>`).
    3. **Wallet Provider Discovery and Trust**: the IT-Wallet ID EAA Provider checks the authenticity and validity of the Wallet Instance, establishing the trust to the Wallet Provider and obtaining Wallet metadata with the parameters required for interoperability needs, according to the Trust Model.
    4. **User Authentication**: For IT-Wallet ID the primary authentication method is based on CieID LoA High (L3). For scenarios where CIE PIN is not immediately available, an alternative authentication method is available combining eID Substantial Authentication along with MRTD Verification. For complete technical specifications, see :ref:`credential-issuance-l2plus:eID Substantial Authentication with MRTD Verification for IT-Wallet ID Issuance`.
    5. **Fetch of IT-Wallet ID data from National Public Registry**: the IT-Wallet ID EAA Provider obtains the required IT-Wallet ID data from National Public Registry (ANPR) which acts as Authentic Source.
    6. **IT-Wallet ID Issuance**: the IT-Wallet ID EAA Provider releases a IT-Wallet ID bound to the key material held by the requesting Wallet Instance.

High-Level EAA flow
----------------------

The :numref:`fig_High-Level-Flow-ITWallet-EAA-Issuance` shows a general architecture and highlights the main operations involved in the issuance of a EAA, following the assumptions listed below:

  - the User has a valid PID or IT-Wallet ID stored in their own Wallet Instance, according to :ref:`pid-until-notification`;
  - the EAA requires a high security implementation profile.

.. _fig_High-Level-Flow-ITWallet-EAA-Issuance:
.. plantuml:: plantuml/eaa-issuance-high-level-flow.puml
    :width: 99%
    :alt: The figure illustrates the general architecture and high level flow for EAA issuance.
    :caption: `EAA Issuance - General architecture and high level flow. <https://www.plantuml.com/plantuml/svg/ZLHXRzis4FskNt4p2im1qZbPqWue7AEkh2m2lDYGdGK50WYCTB49owH6dfAem_xxZb9ZovdIoLyi7X_VUpm-yhCbOQZOPjvFKYLPaI8C_VE1VnxxMf6G2it8ywx2IH0lba4Kp9PVvq7_o9kElyvkbl4qk5p6KVZxrP9hdjr8bGiZjf3nGYfp16rehHiJIgTeCOVJavD6rGYrgQg_dNZUpp311ruFYtaKBeD5mnaLkKZDsI3HswrMevQP1tRzNZoXrLjy_s6Ge27v81D1s06T2XBtmdQ1PZhPT80L5etjubElki2OxH5D1-06ouxkEi1a6YV2f1sG-9oiXLfXB3Bgqc-q6z9v1-IJo3ByNyg1L9Oa5IHTEBnncaQOBSMgtnEsL4dl6DuHFfElCsqktesZQ7ORNywkbx4_cyuYddMnFPXjJYoepF1Y8kmQqocF-qSS-JaQgrNVTV8OUZVyr-F_syekX6n7g0HXhREKPuwytQNgFyd_ujpIMJWv_zCFOG3LrzpLm3ctkP645xsw5SprHHSg5QRivpAT6_qeqyh3F9n0FNIAyBS7_DlhFYPEc1MujisrGaMseUi-UySxiUz7psg7B2Pd73Utb6e5Ss6etDDzP_Dv2uln7zDNZ2xfJFVFtdwOyY99PMCFVXZ852Po9Kbay0AuKt29313kV7TRMvIMS1i7pzINgRFr0jztWOklkS0cQzmYkEkUWbPGIqxr6AxaQWtzwTbHi-kDP5NkTwseX8LbYN51QqUUm48NfZxDyVKyUjM0bqU6QGv9I31mQGfBiE1xBXEq8DI-3Rx1ohp8BFY2Athbg8ERINWxkAwQmgW8LzAIAL-fklUA5Jq-ipgidB_UqCfl-EdqusYOkD032uo6zwEJuU1-D1nKDVvteD6TkXMAs11mldh7FUPoLCn2uasYqrQYPa1vSpRHZsZuSDrUg-qVq7DUt-J_jPK_mhyAj6GFdJBFZwoUjLBLzxF5BRIOvJl10NnJuRnLOHSQGMZl50_0FI8xrlYcSYxicxmVMdbdzovPbWM8ZBmlcBtc_29Vki5-EI4k92HMzg9-8_VT-b52FhPgXjOMs6YxqeHW-3OHw0SWuTNX5WGEMJsCXUK5RjEx_EQ2rfyQzno2-hus6iLLr__z6ZUdZVnMZN_nFEH99-vzvgzYc_qB>`_


.. .. figure:: ../../images/High-Level-Flow-ITWallet-QEAA-Issuance.svg
..     :figwidth: 90%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/ZPJ_Rzgy4yT_pr_XeKgZKccWq2-TsceCw8R46Zv0LqsQ55tYQx0QxCnsQFayUlxtvqo0jfHMYP12xiwlUv_Flg_6WhRvBFK-2HcdEKSsjJOpNtnVm-DX8kmqZtA3EbRIehI7iPhvMGhIhQaPorCH-PrMRUXCjpy7_WoCHKsciADccP9kJURuF_hTNZYUz4QzOF9xsAlkUuFsx-1s4WvwrvDmrF_-OqAspsnbdGJ3i1lStP3DCmz2Pg1Xnb8XqIuoP4hRgV8yzkoIYgF1Z3NgzPTc3VB1cO-QvnxHktXF23OUZlgJtjZxn8llJh_NxzwE1YMA5nPI0Nuii9PeoAOYDdupQhPuetdMmjFZwAnnregYazFxUZrg79sVra_ku_Cch-Dnmn__-kuJI4D8o90OXsQUR5JqEy5DEH4spu3hvdCd17bhznHHCvaM5isg4Pkshk4-BPyfMVJaZND9W4SqQeQrOpz6RSMzYC5YkGKSB4HWIaQdAdue5-dgDoKrgwHa937dgCl5Fk2YhDAoIC7363Gl5unFyHHaWY6ajcGhq3nObPKBVeGqnJ9WNqXZXSsjM9yXhytv2DC99DKAc8MCAmTip-AJxQXKwSkzzcWKt8NNmSqax0I3O4HUTujVULywndQHucKNp1JvWBwh-pG1XgYDabMtkGUiSakl2htlbgfPdoI1Z95DLSh9i__Yefk5iJXZaSeb1xqWnxVLtsfHyrYbosAUSMjBPP_zup5wFhEV82IBr_FCBAsRyLPz56-rE7b1lzlwrUapdot_3PsjSh1NND3BIf6_KFklvsrq_KM0eLPpmPV5Ll-ttsktsTfIMjKyTh8e_xFDl52r9MPr64dDQuhEA8xQkn0oOKFGTl7iT8YTbRahI2GgYfvDUDXxibKm5DhExPGC8gQzpdMnMLk8zI0Xp6k01GgyHeuQN9FO6FLSn6WOICww8d7ZcNKqSfS0KiCwG1QLvEkMrAvxNQOn4SRgnLPMDv0e8prKSd7QgBcL2oF-ZryQ9rSNiJkrZEXN5z5L_SAFhYxyfOtUBkZgZxm3QKaDA_fMEQWGqD48PE5TLcCdQwltL9-9rHpruezqvKvqRkoh3FFuVRb7ErECy6-EnXfAjYMOM1yfRkx45TTWXsBsLd1uIyVhemrkxKonEJrWaMJJ1tC3eS2kk4uxc7V1npl1GMH1I4CPhDKYoWbVGB-9zNxeZ0pkjsSXCPUhWKTfrm4VL7EoCsdVc1otTlyhIawZzJy0

..     (Q)EAA Issuance - General architecture and high level flow

Similarly to the PID and IT-Wallet ID high-level flow, the above diagram depicts a National EAA high-level flow starting from the User who wants to obtain an EAA (step 0). Below the description of the most relevant operations involved in the EAA issuance:

    1. **EAA Provider Discovery and Trust**: the Wallet Unit obtains the list of trusted EAA Providers using the Digital Credential Catalogue and selects exactly one framework for each interaction. A QEAA Provider uses the EUDIW path, while an EAA Provider uses the National path; for an EAA Provider, the Wallet Unit MUST evaluate trust using the Federation Entity Authentication and National Authorization (:ref:`trust-evaluation:Federation Entity Authentication` and :ref:`trust-evaluation:Authorization`) and MUST obtain the applicable final metadata through :ref:`trust-evaluation:Metadata Retrieval and Validation` (:ref:`WP_045–046 <wallet-credential-issuance-testcases>`).
    2. **EAA Request**: the Wallet Unit requests a EAA using either the Authorization Code Grant or the Pre-Authorized Code Grant supported by the EAA Provider (:ref:`WP_051 <wallet-credential-issuance-testcases>`).
    3. **Wallet Provider Discovery and Trust**: the EAA Provider verifies the authenticity and validity of the Wallet Instance. During this step the EAA Provider establishes trust with the Wallet Provider and retrieves Wallet metadata containing the necessary parameters for interoperability, as defined by the Trust Model.
    4. **User Authentication**: the EAA Provider, acting as a Relying Party Instance, authenticates the User evaluating the presentation of the PID or IT-Wallet ID, according to :ref:`pid-until-notification`.
    5. **Obtaining Attributes**: the EAA Provider fetches User attributes from the relevant Authentic Source.
    6. **EAA Issuance**: the EAA Provider releases a EAA bound to the key material held by the requesting Wallet Instance.
