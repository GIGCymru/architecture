# GIG Cymru NHS Wales - Architecture Decision Records

## Building Docs

**WIP**: Publishing our records using a [Mkdoc Material](https://squidfunk.github.io/mkdocs-material/) site

Install 'uv' for Python package/env management e.g. :

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Setup the local environment and install dependencies:

```bash
uv sync
```

Run mkdocs locally:

```bash
uv run mkdocs serve
```

Navigate to ``http://127.0.0.1:8000/``
