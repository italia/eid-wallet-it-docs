.. include:: ../common/common_definitions.rst

.. "included" file, so we start with '-' title level

Soluzione Wallet
----------------

La Wallet Solution è emessa dal Fornitore di Wallet sotto forma di applicazione mobile e servizi, come interfacce web. L'applicazione mobile funge da interfaccia principale per gli Utenti, consentendo loro di conservare i propri Attestati Elettronici e di interagire con altri partecipanti dell'ecosistema, come i Fornitori di Attributi Elettronici e le Relying Party. Questi Attestati Elettronici costituiscono un insieme di dati che possono identificare in modo univoco una persona fisica o giuridica, insieme ad altre Attestazioni Elettroniche Qualificate e non Qualificate di Attributi, note rispettivamente come QEAAs ed EAAs, o più brevemente (Q)EAAs. Una volta che un utente installa l'applicazione mobile sul proprio dispositivo, tale installazione viene definita come istanza del Wallet per quell'utente. Supportando l'applicazione mobile, il Fornitore di Wallet garantisce la sicurezza e l'affidabilità dell'intera Wallet Solution, poiché è responsabile dell'emissione della Wallet App Attestation (WAA) e della Wallet Unit Attestation (WUA). La WAA dimostra l'autenticità e l'integrità dell'istanza del Wallet, mentre la WUA fornisce la prova che le chiavi utilizzate per il collegamento crittografico delle credenziali sono archiviate in modo sicuro all'interno di un WSCD affidabile. Inoltre, la WUA conferma che la Wallet Unit non è stata revocata.

Il seguente diagramma illustra l'Architettura di Alto Livello della Soluzione Wallet.

.. _fig_wallet-solution-high-level-architecture:
.. plantuml:: plantuml/wallet-solution-architecture.puml
    :width: 99%
    :alt: L'immagine illustra la Soluzione Wallet e le sue relazioni e interazioni all'interno dell'ecosistema.
    :caption: `Architettura di Alto Livello della Soluzione Wallet. <https://www.plantuml.com/plantuml/svg/nLVVRo8t47xdht2vgkKaKYu7EH6fEHs1H4Mwqw4ZkJwkZ3tiMjcrjxOtX5RztsjxJRm_2BTvQXwIC9xvvlDuvhFvf3IMkiZIta-CaxIWW7wVJqRpIJGNMIuuSFsnr_iLBM3BEA3rwjloxcPTSTP5ZgaSZuZ8Ci4_7bdP2gxFy0wKoE3iOaH0QhPb16leu9qAyj31hL0WLPVa8kxYPj0UGNPmP3GYMD8Edl144inZY72gExXJK0zQv1qyCx5XwGzBEM9SQQOBpGHt1pelb1OPKdgVWkhDABr98GEkxt0ywCEJ1ibnsX-YdpVnNAH2NlNVNBeVQxF8thfBc0Rd9oG5wQsnX7t_RHCsbop3Sbz7FJ__CDtGJgXltcqcq-ca3Qo024vRq1_8PZpUTeEUuEdu_MKRMij2wJhiT3Q-dDvsWxsuU3--c1dOC4Cw0OI95b8Xp2awr1gflTAGgTuAf19yO5jwYFhtve-1xPTMb8YKCXwZ1OkPDa5p2THGPJXLDhao9TPmrNVpOBAk7MPqywG7RYCHvYGH5lVEVaGp-z7XVnD28x55sjctGZgUoxkpFt6QWaQtG45YspusZyQnkggqISXS6UzwVlBCD69A5I2LoHheesLfj5nEP_0pLqUNaEvDNQ8Sc_IWx8PA2revInVSC25rRAgO2Lx08oEc8bn3R0BsQ0tIMbuBN6y4NzsrIDqwseZ2DNBlslyps3cFI7aFaot4U4pqpt7KbHIFZ894rvWy0ASleszAXm3U32sJFDy9WrqURQNWkWowzV-YPuU-XO8DKcMHobQtlOmEOTR3Pp6hb3Ax5vo629r8KSG9miW2kLXc8kKM4q03sw7mXBCy1RHEn4wDleCqZGTgz0Lp78CwL679bSRS8BuDn-ILg7fANd7D2OLTvfJJ20wC3E7PQcdmF8c-Dy3PmSDP2fq8oVu6YgWVqb04OduhqvM7wy0sACKQ_nQeUIshawlU7ZM6EnQbR0jaJr8moHjRHfyFQwWiIkQFfjAxVs1EqtQra8IOAIrnsNJ6g0irTCSeuL6GXXHucGoCxKrRPUhrHm4fxFGyAz0lQErDlddQ30_d-G1xmw0YC9xF0HDbWZCjf2dg2MBsHM68_NjyPEuDmijZKfXLNsNlw-QYvSTy4Tiduln3KGeM-URmKX-wwsIpbfT-hRwbg5RWIa6jL_Lh3dovc7oVBvtcmry5AAsEtIP82zHMvzDjsZxqN88oVrspLAYjAkRZ15T3j5n_FP--En-VNVH3o8jSwtB_Qg9M08kyGl7Q6Mn_6MYbXOH0zBNWkt3A_yU8_cX6pImqo6eXSMp9kja4j2uD3NbVpsT3P7ulXkWBP4BkcyFgg91mJfsciZcO4bAt4PMmNFLwvfpzqwX-1PdXCNknoz7dXYgsLDpD62PQeHtJIOWAW5s2hfdbqlIhdNKp1hbCzmr-TMNqUt5FC2BtkHQnn7d221AvVu7vZJPWg68-zaLonzvWxOs54ZVboNMBnwxhJJVi47rS6Dglk3Q0Bs6WThhceIM2JxjIjUMMaZObn-kXdS6Z0FNDdOAf2k5Hg5Ew9BqkjN739BGkf33UtHeDcOhxchUVeetl5FuxWd_jYOt69czDfQgtjtq9PeRe9-2qoDB_0000>`_



.. toctree::
  :caption: Indice dei Contenuti della Soluzione Wallet
  :maxdepth: 2

  wallet-solution-requirements.rst
  wallet-solution-components.rst
  wallet-instance.rst
  backup-restore.rst
  wallet-provider-entity-configuration.rst
  wallet-solution-metadata.rst
