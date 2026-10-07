# IT-Wallet agent instructions

This repository is the Sphinx source of the IT-Wallet Technical Specifications (national implementation framework for the Italian Digital Wallet).

## Where content lives

- Published specification: `docs/en/` and `docs/it/` (reStructuredText). Shared link targets live in `docs/common/common_definitions.rst`.
- Examples included from the spec: `examples/`.
- Editorial conventions: `CONTRIBUTING-RULES.md`. Follow them when changing the spec.
- Rules for editing the specification are in `docs/AGENTS.md`. They apply when working under `docs/`.
- Files outside `docs/` (analyses, notes, reports, draft regulations, certification drafts) are working material. Do not copy them into the specification unless asked.

## Languages

The specification is bilingual. A normative or structural change in one language belongs in the other (`docs/en` and `docs/it`) in the same change, unless the request is explicitly single-language.

Both languages use the English BCP 14 keywords (`MUST`, `MUST NOT`, `REQUIRED`, `SHALL`, `SHALL NOT`, `SHOULD`, `SHOULD NOT`, `RECOMMENDED`, `NOT RECOMMENDED`, `MAY`, `OPTIONAL`) only in all capitals. Do not translate those keywords, and do not change their strength unless asked.

## Git

Never create a commit. Never run `git push` or any command that publishes commits to a remote.

## Editing

- Reuse defined terms (Wallet Instance, Credential Issuer, Relying Party, IT-Wallet ID, PID, and so on). Do not introduce synonyms.
- Example hostnames are `example.org` (or a subdomain of it). Do not use real production URLs in examples.
- Keep changes limited to the requested section. Do not rewrite surrounding normative text for style.
