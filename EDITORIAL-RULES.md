# Editorial policies

These policies apply when changing the IT-Wallet Technical Specifications. reStructuredText formatting is in `CONTRIBUTING-RULES.md`.

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

A choice has one keyword. Do not state a set and then, in the next sentence, select a member of that set with another keyword. Split the cases. Each case names the subject and one keyword. The requirement that comes from an external source cites that source. Support for other options is a separate requirement, with its own subject and its own strength.

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

When the same choice is a set in one sentence and one member of that set in the next, at a different strength, split the cases as specified in `Normative language`. Do not leave both sentences. For any other pair of strengths on the same behavior, do not pick one to make them match. Name both places and ask which formulation remains. Do not change a keyword's strength unless asked.

The test states the requirement and does not add a behavior the specification does not state. A `:ref:` to a test identifier must resolve to a row that exists. When the requirement changes, update the purpose, description, and expected result of every test that section cites and of every test that covers the same behavior, in both languages.

A section marked as a draft or work in progress is not a source of requirements for other sections or for tests.

When a sentence you are already editing can be read as two requirements, or its subject is a pronoun, split it and name the defined term. Leave neighboring normative sentences as they are.

## Test plans

When the requirements of a section change, update the test cases that section cites, and any other test case that covers the same behavior, in the same change and in both languages. The test states the current requirement. A test that no longer applies keeps its identifier. Empty its purpose, description, and expected result with `Voided` in English and `Annullato` in Italian. Do not delete the row, and do not reuse the identifier.

## Sentences

Do not join clauses with a semicolon. Use separate sentences.

## Clarity index

Clarity is measured by the editorial clarity index in `.github/scripts/clarity_index.py`. A scored document starts at 100 and loses:

- up to 40 points for the share of sentences longer than 35 words, at 1.2 points per percent
- up to 30 points for semicolons per 1 000 words, at 6 points each
- up to 30 points for sentences that contain two or more normative keywords per 1 000 words, at 12 points each

Directives, their options (`:language:`, `:caption:`, `:sorted:`, and the same kind of line), literals, and test plans are not scored. The indentation of that markup is not scored either. A document with fewer than 8 sentences after that removal is not scored. Every scored document must be at least 90.

## Certificate chain

The ordered set of X.509 certificates built from an end-entity certificate toward a Trust Anchor is a certificate chain. In English write certificate chain. Do not write certification path or certificate path for that set. In Italian write catena di certificati. Do not write certification path, certificate path, percorso di certificazione, or percorso del certificato for that set.

The algorithm input named ``path`` keeps that name. A trust-framework route, such as the EUDIW path or the National path, is not a certificate chain.

## Defined terms and acronyms

In `defined-terms.rst` (the glossary and the Acronyms table), describe the term. Do not use BCP 14 keywords there. Do not use a `:ref:`, a hyperlink, or any other reference to another part of the specification. Defined terms sit above the rest of the specification and must not depend on a section. Put the requirement in the body of the specification.

Write defined terms as they are defined in `defined-terms.rst`, including capitalization, in both editions. In English the defined term is Credential and its plural is Credentials. In Italian the defined term is Credenziale and its plural is Credenziali. Write that capital even mid-sentence. The ordinary phrases authentication credentials and credenziali di autenticazione are not that term. JSON member names and protocol parameter names stay as specified.

## Bold is not a heading

A line whose whole content is a bold title introduces the text below. The title may be `**Status List**`, `**Taxonomy Objectives:**`, or `**Input Variables**:` with the colon outside the bold. Sphinx does not index that line, and `:ref:` cannot point to it. Replace it in both editions.

When the line labels a non-normative example, replace it with a sentence. The sentence stays out of the table of contents. The title of a `.. note::` is the argument of the directive.

```rst
The following non-normative example is the EUDIW Request Object that uses ``x509_hash``.

.. note:: Why the response is encrypted?
```

When the line names a part of a section, make it the next heading level after its parent. The levels, in order, are `=`, `-`, `^`, `"`, `.`. The underline is at least as long as the title. The title is unique in that document. When the same short label repeats, such as Input, Outcome, or Process, prefix it with the parent title, as in `EUDIW Authentication: Input`. When that prefixed title would still repeat, give the later heading its own title, as in `Authorization Validation: Final Outcome`.

Keep the bold in these cases:

- the names of the terms in `defined-terms.rst`
- the header cells of a `list-table`
- a run-in label that continues in the same paragraph or list item, such as `**Step 12**:` followed by the sentence, or `- **Same Device**:` inside a list
- a term emphasized in the middle of a sentence

## reStructuredText

Apply `CONTRIBUTING-RULES.md`. Heading underline length must be at least the title. Levels, in order: `=`, `-`, `^`, `"`, `.`. A line of bold is not a heading. Follow `Bold is not a heading`.

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
