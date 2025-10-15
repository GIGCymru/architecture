# GIG Cymru NHS Wales - Architecture

[![mkdocs](https://github.com/GIGCymru/architecture/actions/workflows/publish.yml/badge.svg)](https://github.com/GIGCymru/architecture/actions/workflows/publish.yml)

The documents in this repository are published to [https://gigcymru.github.io/architecture/](https://gigcymru.github.io/architecture/).

## Introduction

This repository hosts architecture related content and decisions, such as
architecture principles, architecture decision records (ADRs) and governance
information.

## Getting Started

There are several ways to set up your development environment:

### 1. GitHub Codespaces (Recommended)

The fastest way to start contributing:

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/GIGCymru/architecture?quickstart=1)

This provides:

* A pre-configured VS Code environment (with useful extensions installed)
* All required dependencies installed
* Automatic port forwarding for preview
* Git integration

Once you have successfully launched Codespaces you can run the
development server from the VS Code Terminal:

```bash
    uv run mkdocs serve
```

You will be prompted to **Open in Browser** to view the locally running site.

See the [Quickstart Guide](http://docs.github.com/en/codespaces/quickstart) for
more information.

Note: It can take a few minutes to fully launch Codespaces the first time, but
is faster on subsequent launches as the environment is then cached.

### 2. Local Development

**Prerequisites:**

* Python 3.11 or higher
* [uv](https://github.com/astral-sh/uv) for package/env management
* [npm](https://github.com/npm/cli) for markdown linting
* Git

**Setup Steps:**

Clone the repository:

```bash
    git clone git@github.com:GIGCymru/architecture.git
    cd architecture
```

Install uv (if not already installed):

```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
```

Set up environment and dependencies:

```bash
    uv sync
```

Start the development server:

```bash
    uv run mkdocs serve
```

View the documentation at: ``http://127.0.0.1:8000/``

### 3. Container-based Development

If you prefer using containers:

**Prerequisites:**

* [Podman](https://podman.io/) or [Docker](https://www.docker.com/)

**Setup Steps:**

Build the container:

```bash
    podman build --tag mkdocs .
```

Run the development server:

```bash
    podman run -p 8000:8000 mkdocs
```

View the documentation at: ``http://127.0.0.1:8000/``

### 4. Make-based Workflow

For those familiar with Make:

```bash
    # See available commands
    make help

    # Full build and serve
    make
```

View the documentation at: ``http://127.0.0.1:8000/``

## Linting

This project uses `markdownlint-cli2` to lint the markdown files in the `doc/` directory.

To run the linter, you will first need to install it using `npm`:

```bash
npm install
```

Once it is installed, you can run the linter by running the following command:

```bash
make lint
```

This will check all the markdown files in the `doc/` directory and report any errors.

## Documentation

Our documentation is built using [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

## Contributing

1. Choose your preferred development environment from above
2. Create a new branch for your changes
3. Make your changes
4. Test your changes locally
5. Submit a Pull Request

## Further Reading

* [Why write architecture decision records - By GitHub Engineering](https://github.blog/engineering/architecture-optimization/why-write-adrs/)
* [A practical overview on Architecture Decision Records](https://ctaverna.github.io/adr/)

## License

This repository is licensed under the [MIT License](LICENSE)
