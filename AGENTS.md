# IT-Wallet agent instructions

This repository is the Sphinx source of the IT-Wallet Technical Specifications (national implementation framework for the Italian Digital Wallet).

## Where content lives

- Published specification: `docs/en/` and `docs/it/` (reStructuredText). Shared link targets live in `docs/common/common_definitions.rst`.
- Examples included from the spec: `examples/`. An example that is the same in English and Italian (code, JSON, HTTP, or any other sample) belongs in `examples/` and is included from both `docs/en` and `docs/it` with `literalinclude`. Do not paste that example into both language files.
- Editorial conventions: `CONTRIBUTING-RULES.md`. Follow them when changing the spec.
- Rules for editing the specification are in `docs/AGENTS.md`. They apply when working under `docs/`.
- Files outside `docs/` (analyses, notes, reports, draft regulations, certification drafts) are working material. Do not copy them into the specification unless asked.

## Languages

The specification is bilingual. A normative or structural change in one language belongs in the other (`docs/en` and `docs/it`) in the same change, unless the request is explicitly single-language.

The English edition uses the English BCP 14 keywords (`MUST`, `MUST NOT`, `REQUIRED`, `SHALL`, `SHALL NOT`, `SHOULD`, `SHOULD NOT`, `RECOMMENDED`, `NOT RECOMMENDED`, `MAY`, `OPTIONAL`) only in all capitals. The Italian edition translates them and keeps them in all capitals, with number agreement: `DEVE` and `DEVONO`, `NON DEVE` and `NON DEVONO`, `PUÒ` and `POSSONO`, `DOVREBBE` and `DOVREBBERO`, `NON DOVREBBE` and `NON DOVREBBERO`, `RACCOMANDATO`, `NON RACCOMANDATO`, `OBBLIGATORIO`, `OPZIONALE`. Do not change their strength unless asked.

## Git

Never create a commit. Never run `git push` or any command that publishes commits to a remote.

## Editing

- Reuse defined terms (Wallet Instance, Credential Issuer, Relying Party, IT-Wallet ID, PID, and so on). Do not introduce synonyms.
- When a sentence uses a normative keyword, name the subject before the keyword. Do not start the sentence with the keyword. Do not use a pronoun as that subject. Repeat the defined term, as in `The Wallet Instance MUST` and `La Wallet Unit DEVE`.
- Write defined terms as they are defined in `defined-terms.rst`, including capitalization, in both editions. In English the defined term is Credential and its plural is Credentials. In Italian the defined term is Credenziale and its plural is Credenziali. Write that capital even mid-sentence. The ordinary phrases authentication credentials and credenziali di autenticazione are not that term. JSON member names and protocol parameter names stay as specified.
- In `defined-terms.rst`, describe the term and stop there. Do not use a `:ref:`, a hyperlink, or any other reference to another part of the specification. Defined terms sit above the rest of the specification and must not depend on a section.
- Example hostnames are `example.org` (or a subdomain of it). Do not use real production URLs in examples.
- Keep changes limited to the requested section. Do not rewrite surrounding normative text for style.
- When the requirements of a section change, update the test cases that section cites, and any other test case that covers the same behavior, in the same change and in both languages. The test states the current requirement. A test that no longer applies keeps its identifier. Empty its purpose, description, and expected result with `Voided` in English and `Annullato` in Italian. Do not delete the row, and do not reuse the identifier.
