# justfile for GIG Cymru NHS Wales - Architecture project
#
# This justfile provides commands for building, serving, and managing the
# architecture documentation site built with Zensical.
#
# Quick start:
#   just          - Run the full setup and start the dev server
#   just --list   - Show all available commands
#   just --help   - Show Just command-line help

# Project URLs
local_url := "http://127.0.0.1:8000"
prod_url := "https://gigcymru.github.io/architecture"

# ============================================================================
# Development Workflow
# ============================================================================

# Run full setup: install dependencies, sync environment, build site, and start server
default: install sync build run

# Display all available commands with descriptions
help:
    @just --list

# ============================================================================
# Setup & Dependencies
# ============================================================================

# Install uv package manager (required for Python dependency management)
install:
    @echo "📦 Installing uv package manager..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    @echo "✅ uv is now installed and ready to use"
    @echo "   Run 'just sync' to install project dependencies"

# Synchronize Python dependencies using uv (creates/updates virtual environment)
sync:
    @echo "🔄 Synchronizing project dependencies with uv..."
    uv sync
    @echo "✅ Dependencies installed and virtual environment configured"
    @echo "   Run 'just build' to build the documentation site"

# ============================================================================
# Documentation Building & Serving
# ============================================================================

# Build the documentation site (output to ./site directory)
build:
    @echo "🏗️  Building documentation site with Zensical..."
    uv run zensical build
    @echo "✅ Documentation site built successfully"
    @echo "   Output: ./site/"
    @echo "   Run 'just run' to start the local server"

# Start the local development server (auto-reloads on file changes)
run:
    @echo "🚀 Starting local development server..."
    @echo "📖 Documentation will be available at: {{local_url}}"
    @echo "   Press Ctrl+C to stop the server"
    uv run zensical serve

# ============================================================================
# Deployment
# ============================================================================

# Build and deploy documentation to GitHub Pages (requires push permissions)
deploy:
    @echo "🚀 Building and deploying to GitHub Pages..."
    uv run zensical build
    @echo "📤 Pushing to gh-pages branch..."
    uv run ghp-import -n -p -f -m "Update documentation" site
    @echo "✅ Documentation deployed successfully!"
    @echo "🌐 Live site: {{prod_url}}"

# ============================================================================
# Quality Assurance
# ============================================================================

# Run markdown linter on all documentation files (requires npm install)
lint:
    @echo "🔍 Linting markdown files with markdownlint-cli2..."
    npx markdownlint-cli2 "doc/**/*.md" --config .markdownlint-cli2.jsonc
    @echo "✅ Markdown linting complete - no issues found!"

# ============================================================================
# Document Conversion
# ============================================================================

# Convert markdown templates to Word documents using Pandoc
word:
    @echo "📄 Converting markdown templates to Word format..."
    @echo "   Converting: architecture-decision-record-template.md"
    pandoc doc/design-authority/dhcw/architecture-decision-record-template.md --reference-doc=.github/workflows/markdown-to-word-styles.docx -o architecture-decision-record-template.docx
    @echo "   Converting: architecture-design-overview-template.md"
    pandoc doc/design-authority/dhcw/architecture-design-overview-template.md --reference-doc=.github/workflows/markdown-to-word-styles.docx -o architecture-design-overview-template.docx
    @echo "✅ Word documents generated successfully!"
    @echo "   Output: architecture-decision-record-template.docx"
    @echo "   Output: architecture-design-overview-template.docx"
