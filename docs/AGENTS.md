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

## Normative language

State each requirement in one place. Do not give the same object conflicting keywords in different sections (a `MUST` in one place and a `SHOULD` or `MAY` for the same behavior in another). Do not put conflicting keywords in the same sentence. One sentence states one requirement.

```rst
The Wallet Instance MUST reject an expired Credential.

See :ref:`credential-revocation:Credential Status`.
```

## Test plans

When the requirements of a section change, update the test cases that section cites, and any other test case that covers the same behavior, in the same change and in both languages. The test states the current requirement. A test that no longer applies keeps its identifier. Empty its purpose, description, and expected result with `Voided` in English and `Annullato` in Italian. Do not delete the row, and do not reuse the identifier.

## Sentences

Do not join clauses with a semicolon. Use separate sentences.

## Defined terms and acronyms

In `defined-terms.rst` (the glossary and the Acronyms table), describe the term. Do not use BCP 14 keywords there. Put the requirement in the body of the specification and, if needed, point to that section from the definition.

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
