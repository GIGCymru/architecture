# Lint

**Status**: first sketch, work in progress, request for collaboration

**Date**: Updated 2025-04-04

**Governance**: Chris & Joel for now because this is so lightweight.

## Context

We want to use a lint program for our documentation, because it's helpful if there's an automatic lint step that checks our work for common mistakes.

## Drivers

Broadly, we want use lint programs in many ways to improve quality.

Specifically, we want to add a lint tool:

* Right now.

* Installable locally so we're not sending data elsewhere.

* For VS Code because we both use it

* With a good rating in the VS Code marketplace.

* Focusing on our immediate need for writing markdown.

* With a configuration file that we can check into this git repository.
  
## Assessment - Considered Options

### markdownlint

<https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint>

It focuses on markdown, and is very popular.

It's fast and configurable, and the configuration file can be checked into a git repository as a file `.markdownlint.json` so it's usable by all the people who use the repo with VS Code or any other editor that uses the same file.

### trunk.io

<https://marketplace.visualstudio.com/items?itemName=trunk.io>

It handles many languages simultaneously.

It offers many more features than linting.

TODO learn more about this.

## Recommendation - Decision Outcome

Adopt markdownlint for right now.

Commit the file `.markdownlint.json` to the top level of this repo.

Revisit if/when a teammate is ready to research if there's something better.
