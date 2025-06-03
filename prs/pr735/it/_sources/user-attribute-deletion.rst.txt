.. include:: ../common/common_definitions.rst


Eliminazione degli Attributi dell'Utente
========================================

Questa funzionalità dell'Istanza del Wallet consente agli Utenti di ottenere un elenco di tutte le Relying Party a cui sono stati presentati attributi che possono identificare univocamente gli Utenti (ad esempio, l'attributo tax_id_code dell'Attestato Elettronico di Dati di Identificazione Personale). Successivamente, gli Utenti possono richiedere l'eliminazione di tutti gli attributi presentati a una Relying Party di loro scelta. Di seguito viene presentato il flusso di alto livello relativo a questa interazione.

.. plantuml:: plantuml/user-deletion-attribute-flow.puml
    :width: 99%
    :alt: La figura illustra il Processo di Eliminazione degli Attributi dell'Utente.
    :caption: `Processo di Eliminazione degli Attributi dell'Utente. <https://www.plantuml.com/plantuml/svg/TLFDZjD03BxdAQnUkB3x03sWNR55ue8G2-B2nKcSTaGw3cDFIzyUUqeIfkpUHlNdxyTVyo2AIVDnX2SQIGD7u06-2QKt0e-gARHPIHhCoZ4VMqeDTie9DexP00faUpHDox_djISwXOwQoOX35oQC2fllE1ezV8oc5pigYpXDKAES01xt5FNAZ0t57epwol-5nak8U_XiEvTwSvTGSYBOnPx3ttMYIMlK1-efeQTquBGW1qEkKb0YmTqxTxWrpoV-IO3pCQ2VBpNasFa3ns1-mE6-vTjRU3xm6SOW2ZnKpWC9_8WXmiGY9FBApMzjF9jgfw07gky0oaQNw5SckOxxjSdLjQp-FEss9Z7XtNlxgP0qK21mDqkNaKmSXVmwaPM0JvHysW00V3NLcuQ1MyKGNHQAgxcX-V0m93xwf22EfDYZedd-Fw8Xl1pNRTOORkr5vP7tVk5_HTTaSqUuzGEZlydlyGAqYkfTl2tG9N5T0sOJZ1ewL9AImHkzByXXv3DqRDDet70su8A00mgqH14aTns937aSQxh-lhv0iR4wBrykhLLx-9QpuPKNcMMhX5_YLiLcN3g__JT_OWt3vShqO5RoSVm3>`_


.. .. figure:: ../../images/user's_data_deletion_flow.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/png/RLBDZjD03BxdAQozS67t0Nf0ksABn0KX5iI5YvCuxOZfE8mzBNrxx2bDcBAtTFpv-_7NHr7CMWwnmwASog6dtE6WdE7kcr2-0nGeOezTpx_1dzu8FDCn3DJDjXg6C6DIkFkECPB2nsICQQ2wYFCCBSe9u6b7II_Cs54QmQWl_5yedaFQmMVRERURsunICi4sZHp-hXFDsg8-q4WPDN1ouBmW9qSkKb0ZmVqxTxWnpqV-IO2gEVH52KQAL3ccaWR_m1ZC3pZSjtnx0ozxFa4Cei1JupoGm8yK4imiGYBEnDFrU4zNcLiRBwOwAEYUsZk0ij5b-bL8wdZrnzFgMbP_ddRJafZmzhqzLH93EWJkhz9r93Cd8RzEOYNW8sMVsc-0hwPwqp1mhnYIrBcxMXkw71wcp0UVLCI154TKDC__HpI4b-EwtHh3hRsg77dd5_vNT4csT8GRFp3wD_azNe4sKRsBjnMw96vhm6A2ISE0Ib8pUACF5Jb5Fi70Dat63IS3BWZOeq1FzY9b64XaAZ6sTED3Uu5gOtN-x7tJMhM7xxaONdcHMRPg-2LkKsp1fVFRV_CdrZ2TBqoFPgKSuXy0

..     Sequence Diagram for Deletion of User's Attributes

**Passo 1:** L'Utente richiede l'eliminazione degli attributi invocando la funzione di eliminazione degli attributi dell'Istanza del Wallet.

**Passo 2:** L'Istanza del Wallet raccoglie tutti i dati delle transazioni e mostra all'Utente l'elenco delle Relying Party con cui ha avuto interazioni durante il ciclo di vita dell'Istanza del Wallet e che sono in possesso degli attributi dell'Utente. L'Istanza del Wallet DOVREBBE filtrare i log delle transazioni in modo che vengano mostrate solo le Relying Party che hanno avuto accesso ad attributi che identificano univocamente l'Utente.

**Passo 3:** L'Utente seleziona la Relying Party di destinazione per l'eliminazione degli attributi.

**Passi 4 - 5:** L'Istanza del Wallet ottiene la Entity Configuration della Relying Party all'endpoint ./well-known/ della Federazione. L'URL o l'Endpoint di Cancellazione (``erasure_endpoint``) può essere trovato all'interno del parametro dei metadati.

**Passo 6:** L'Istanza del Wallet registra le informazioni rilevanti della Richiesta di Cancellazione. Questi log DEVONO includere almeno:
  * la data della richiesta,
  * la Relying Party a cui è stata fatta la richiesta,
  * gli attributi di cui è stata richiesta la rimozione.

**Passi 7 - 8:** L'Istanza del Wallet reindirizza l'Utente all'Endpoint di Cancellazione. DEVE inoltre garantire che sia presente un meccanismo di callback per consentire all'User-Agent di notificare all'Istanza del Wallet (e quindi all'Utente) dopo la Risposta di Cancellazione. I dettagli sulla Richiesta di Cancellazione si trovano in :ref:`relying-party-endpoint:Richiesta di Cancellazione`.

.. note::
  La pagina web della Relying Party autenticherà l'Utente con un Livello di Garanzia appropriato utilizzando qualsiasi metodo come CIE o la presentazione dell'Attestato Elettronico di Dati di Identificazione Personale. Il meccanismo specifico utilizzato per l'autenticazione è lasciato alla Relying Party. Dopo aver autenticato l'Utente, la Relying Party PUÒ richiedere all'Utente di eseguire ulteriori passaggi necessari per l'eliminazione degli attributi, ad esempio, potrebbe richiedere all'Utente di confermare l'operazione di eliminazione.

**Passo 9:** Dopo aver autenticato con successo l'Utente, la Relying Party DEVE eliminare tutti gli attributi legati all'Utente in suo possesso.

**Passo 10:** La Relying Party restituisce la Risposta di Cancellazione sotto forma di Risposta HTTP all'User-Agent e include l'URL di callback se fornito nella Richiesta di Cancellazione. I dettagli sulla Risposta di Cancellazione si trovano in :ref:`relying-party-endpoint:Risposta di Cancellazione`.

**Passi 11 - 12:** L'User-Agent utilizza il metodo implementato per restituire la Risposta di Cancellazione all'Istanza del Wallet. Infine, l'Utente viene notificato tramite l'Istanza del Wallet riguardo all'esito della Risposta di Cancellazione.
