# IT-Wallet agent instructions

This repository is the Sphinx source of the IT-Wallet Technical Specifications (national implementation framework for the Italian Digital Wallet).

## Where content lives

- Published specification: `docs/en/` and `docs/it/` (reStructuredText). Shared link targets live in `docs/common/common_definitions.rst`.
- Examples included from the spec: `examples/`. An example that is the same in English and Italian (code, JSON, HTTP, or any other sample) belongs in `examples/` and is included from both `docs/en` and `docs/it` with `literalinclude`. Do not paste that example into both language files.
- Editorial conventions: `CONTRIBUTING-RULES.md`. Follow them when changing the spec.
- Editorial policies: `EDITORIAL-RULES.md`. Follow them when changing the spec.
- Files outside `docs/` (analyses, notes, reports, draft regulations, certification drafts) are working material. Do not copy them into the specification unless asked.

## Languages

The specification is bilingual. A normative or structural change in one language belongs in the other (`docs/en` and `docs/it`) in the same change, unless the request is explicitly single-language.

The English edition uses the English BCP 14 keywords (`MUST`, `MUST NOT`, `REQUIRED`, `SHALL`, `SHALL NOT`, `SHOULD`, `SHOULD NOT`, `RECOMMENDED`, `NOT RECOMMENDED`, `MAY`, `OPTIONAL`) only in all capitals. The Italian edition translates them and keeps them in all capitals, with number agreement: `DEVE` and `DEVONO`, `NON DEVE` and `NON DEVONO`, `PUÒ` and `POSSONO`, `DOVREBBE` and `DOVREBBERO`, `NON DOVREBBE` and `NON DOVREBBERO`, `RACCOMANDATO`, `NON RACCOMANDATO`, `OBBLIGATORIO`, `OPZIONALE`. Do not change their strength unless asked.

## Git

Never create a commit. Never run `git push` or any command that publishes commits to a remote.

## Editing

Follow `EDITORIAL-RULES.md` when changing the specification. Follow `CONTRIBUTING-RULES.md` for reStructuredText formatting.

Keep changes limited to the requested section. Do not rewrite surrounding normative text for style.
