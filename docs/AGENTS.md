# Editing the specification

## Cite standards by reference

Do not link a technical specification or standard with a raw hyperlink (`Title <https://...>`_, a bare URL, or an anonymous link).

Define the target once in `docs/common/common_definitions.rst` and cite the name:

```rst
.. _OpenID4VCI: https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html

See `OpenID4VCI`_.
See Section 7.2 of [`OpenID4VCI`_].
As defined in :rfc:`7519`.
```

RFCs use the `:rfc:` role and do not need an entry in `common_definitions.rst`. This does not apply to example hostnames (`example.org`) or to PlantUML preview URLs in a figure `:caption:`.

## Say it once

Do not copy the same requirement or explanation into several places. Put it in one section and point to it with `:ref:`.

## Section openings

The opening of a chapter that introduces other sections orients the reader. It names what the chapter covers and points to the section that owns each topic, with `:ref:`.

Do not use a BCP 14 keyword in that opening. In English that is `MUST`, `MUST NOT`, `REQUIRED`, `SHALL`, `SHALL NOT`, `SHOULD`, `SHOULD NOT`, `RECOMMENDED`, `NOT RECOMMENDED`, `MAY`, and `OPTIONAL`. In Italian that is `DEVE`, `DEVONO`, `NON DEVE`, `NON DEVONO`, `PUÒ`, `POSSONO`, `DOVREBBE`, `DOVREBBERO`, `NON DOVREBBE`, `NON DOVREBBERO`, `RACCOMANDATO`, `NON RACCOMANDATO`, `OBBLIGATORIO`, and `OPZIONALE`.

Do not restate a procedure the owning section already specifies. A pointer is enough.

Put technical detail in the section that owns the behavior. Identity matching belongs in `identity-matching`. Offline presentation and the storage of the bound private keys belong in the Keystore requirements. Consumption of a batch Credential belongs in the Authorization Response of the remote flow. Invocation of the Wallet Instance belongs in Steps 4-7 of the remote flow. The opening of Digital Credential Presentation lists the remote flow and the proximity flow and points to those sections. It does not treat identity matching as a presentation flow.

When a requirement sits only in such an opening, move it to the owning section. Do not drop it. Leave its strength unchanged.

A section that owns a requirement states that requirement in its own text, including near the start of that section. This rule applies to the orienting opening, not to the section that owns the behavior.

## Normative language

State each requirement in one place. Do not give the same object conflicting keywords in different sections (a `MUST` in one place and a `SHOULD` or `MAY` for the same behavior in another). Do not put conflicting keywords in the same sentence. One sentence states one requirement.

Name the subject before the normative keyword. Do not start a sentence with the keyword. Do not use a pronoun as that subject. Repeat the defined term.

```rst
The Wallet Instance MUST reject an expired Credential.

La Wallet Unit DEVE rifiutare una Credenziale scaduta.

See :ref:`credential-revocation:Credential Status`.
```

## Coherence of a change

Before adding or editing a normative sentence, apply the checks below in both `docs/en` and `docs/it`.

Search both editions for the same behavior, including `architecture-overview.rst` and `functionalities.rst`. If the requirement already exists, point to it with `:ref:` and do not restate it. Those two chapters describe the system and cite the normative section. They are not a second place for the requirement.

The English sentence and the Italian sentence state the same behavior. Pair the keywords: `MUST`/`DEVE` and `DEVONO`, `MUST NOT`/`NON DEVE` and `NON DEVONO`, `SHOULD`/`DOVREBBE` and `DOVREBBERO`, `SHOULD NOT`/`NON DOVREBBE` and `NON DOVREBBERO`, `MAY`/`PUÒ` and `POSSONO`, `REQUIRED`/`OBBLIGATORIO`, `RECOMMENDED`/`RACCOMANDATO`, `NOT RECOMMENDED`/`NON RACCOMANDATO`, `OPTIONAL`/`OPZIONALE`. Do not update one edition and leave the other with a different meaning or a different strength.

If the same behavior already uses two different strengths, do not pick one to make them match. Name both places and ask which formulation remains. Do not change a keyword's strength unless asked.

The test states the requirement and does not add a behavior the specification does not state. A `:ref:` to a test identifier must resolve to a row that exists. When the requirement changes, update the purpose, description, and expected result of every test that section cites and of every test that covers the same behavior, in both languages.

A section marked as a draft or work in progress is not a source of requirements for other sections or for tests.

When a sentence you are already editing can be read as two requirements, or its subject is a pronoun, split it and name the defined term. Leave neighboring normative sentences as they are.

## Test plans

When the requirements of a section change, update the test cases that section cites, and any other test case that covers the same behavior, in the same change and in both languages. The test states the current requirement. A test that no longer applies keeps its identifier. Empty its purpose, description, and expected result with `Voided` in English and `Annullato` in Italian. Do not delete the row, and do not reuse the identifier.

## Sentences

Do not join clauses with a semicolon. Use separate sentences.

## Defined terms and acronyms

In `defined-terms.rst` (the glossary and the Acronyms table), describe the term. Do not use BCP 14 keywords there. Do not use a `:ref:`, a hyperlink, or any other reference to another part of the specification. Defined terms sit above the rest of the specification and must not depend on a section. Put the requirement in the body of the specification.

Write defined terms as they are defined in `defined-terms.rst`, including capitalization, in both editions. In English the defined term is Credential and its plural is Credentials. In Italian the defined term is Credenziale and its plural is Credenziali. Write that capital even mid-sentence. The ordinary phrases authentication credentials and credenziali di autenticazione are not that term. JSON member names and protocol parameter names stay as specified.

## reStructuredText

Apply `CONTRIBUTING-RULES.md`. Heading underline length must be at least the title. Levels, in order: `=`, `-`, `^`, `"`, `.`.

`autosectionlabel_prefix_document` is on, so internal refs are `document-stem:Section Title`. Reference names are case-sensitive. The trailing underscore is required.

```rst
See :ref:`wallet-solution:Federation Endpoint`.
```

JSON fields and HTTP parameters are wrapped in double backticks in the RST source, as in ``client_id`` and ``redirect_uri``.

Static images need both SVG (HTML) and PDF (LaTeX), selected with `.. only:: format_html` and `.. only:: format_latex`. PlantUML sources live in `plantuml/*.puml` and use the `plantuml` directive. Every figure has an `:alt:` and a label `.. _fig_name:`.

Use `list-table` with `:widths:`, `:header-rows: 1`, bold headers, and a label `.. _table_name:`.

An example that is the same in English and Italian (code, JSON, HTTP, or any other sample) belongs in `examples/`. Include it from both language files with `literalinclude`. Do not paste that example into both `docs/en` and `docs/it`. Mark examples as non-normative in the surrounding text.

```rst
.. literalinclude:: ../../examples/request-object-header.json
   :language: JSON
```
