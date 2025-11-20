# NHS Wales Architecture Documentation Site

This repository contains the source for the GIG Cymru architecture documentation
website. The following instructions are for an autonomous AI agent to work with
this repository.

## Environment Setup

- install the `uv` package manager if not already installed: `make install`
- install the required packages: `make sync`
- install the `markdownlint-cli2` tool for linting docs: `npm install`

## Running Locally

- execute `make build` to verify the site builds successfully.
- execute `make run` to run the site locally, it will be available at `http://127.0.0.1:8000/`

## Conventions

- All documentation (in Markdown format) to be published on the site lives under the `doc/` path.
- Markdown documents should adhere to a 120 character line limit, unless it breaks URLs/links/special elements.
- See `doc/decisions/meta-decisions/architecture-decision-records-naming-conventions/index.md` for ADR naming conventions and rules.
- Mermaid is used to add diagrams to Markdown files, see `doc/decisions/meta-decisions/use-mermaid-for-documenting-diagrams/index.md` for information.
- Architecture Decision Records (ADRs) reside under the `doc/decisions/` path.
- Architecture Principles reside under the `doc/principles/` path.
- ADRs should follow the agreed template found here: `doc/design-authority/dhcw/architecture-decision-record-template.md`

## PR instructions

- Always run `make lint` before committing and fix any lint issues.
- Always run `make build` before committing and fix any WARNINGS raised.
