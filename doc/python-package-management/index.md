# Python Package Management

!!! info

    **Status**: Proposed
    
    **Level**: 2

    **Updated**: 2025-06-03

## Summary

Python projects require effective dependency and virtual environment management
to ensure reproducibility, reliable dependency resolution, and efficient
development workflows. This ADR evaluates and recommends tooling for managing
Python packages and environments across projects, with a focus on
reproducibility, ease of use, and maintainability.

## Drivers

We need to standardise Python package management tooling because:

* Current ad-hoc approach leads to inconsistent environments and dependency conflicts
* Multiple tools in use create confusion and maintenance overhead
* Need for reproducible builds and deterministic environments across CI/CD
* Requirements for fast, reliable dependency resolution
* Need for lock file support to ensure consistent environments
* Development experience needs improvement with simpler workflows

Our key priorities are:

1. Reproducibility: Guaranteed consistent environments via lock files
2. Developer Experience: Simple CLI, minimal config, efficient workflows
3. CI/CD Compatibility: Works well with our deployment pipelines
4. Community Support: Mature tooling with good documentation
5. Performance: Fast dependency resolution and installation

## Options

We evaluated these popular Python package management tools:

* [`uv`](https://github.com/astral-sh/uv) - Modern, fast package installer and resolver
* [`poetry`](https://python-poetry.org/) - Comprehensive Python packaging tool
* [`pip + venv + pip-tools`](https://pip.pypa.io/) - Standard Python tooling
* [`pipenv`](https://pipenv.pypa.io/) - Unified dependency management
* [`conda`](https://docs.conda.io/) - Cross-platform package manager
* [`hatch`](https://hatch.pypa.io/) - Modern project management tool

## Options Analysis

### `uv`

* Pro: Extremely fast performance (Rust implementation)
* Pro: Full pyproject.toml support with lock file generation
* Pro: Drop-in replacement for pip and pip-tools
* Pro: Compatible with existing Poetry and pip lock files
* Pro: Combined environment and dependency management
* Con: Newer tool with evolving feature set
* Con: Limited plugin ecosystem currently

### `poetry`

* Pro: Complete solution for dependency management and publishing
* Pro: Mature tool with extensive documentation
* Pro: Strong lock file support and reproducibility
* Pro: Native pyproject.toml support
* Con: Complex configuration for monorepos
* Con: Strict/opinionated approach limits flexibility
* Con: Slower dependency resolution

### `pip + venv + pip-tools`

* Pro: Standard Python ecosystem tools
* Pro: Maximum flexibility and control
* Pro: Lightweight, no external dependencies
* Pro: Universal compatibility (CI, Docker, legacy systems)
* Con: Manual setup process prone to errors
* Con: Requires multiple tools working together (e.g. for lockfile management)
* Con: Slower dependency resolution
* Con: Poor developer experience for larger projects

### `pipenv`

* Pro: Combined environment and dependency management
* Pro: User-friendly command line interface
* Pro: Creates lockfiles and manages `Pipfile`
* Con: Declining maintenance and community support
* Con: Slower and inconsistent dependency resolution
* Con: No pyproject.toml support

### `conda`

Overall: I love conda and it's great for AI/ML work, but didn't play well with
other kinds of python projects such as Django apps and Flask services.

* Pro: Excellent for data science/ML dependencies
* Pro: Fast binary package installation
* Pro: Handles non-Python dependencies well
* Con: Not standard for Python-only projects
* Con: Large environment footprint
* Con: Limited lock file capabilities

### `hatch`

* Pro: Modern `PEP 517/518` compliant tooling
* Pro: Strong environment management
* Pro: Good for Python packaging and monorepos
* Con: Smaller community and adoption
* Con: May be excessive for basic dependency management
* Con: Limited evaluation due to newer adoption

## Recommendation

We recommend adopting `uv` as the standard Python package management tool for
projects.

The decision is based on:

* Superior performance and reliability compared to alternatives
* Strong support for modern Python packaging standards
* Excellent lock file support ensuring reproducibility
* Simple drop-in replacement for existing tools
* Growing community adoption and active development

### Consequences

* Pro: Significant performance improvements in CI/CD
* Pro: Simplified developer workflows
* Pro: Better reproducibility via reliable lock files
* Con: Some learning curve for teams used to other tools
* Con: May need to maintain compatibility with legacy projects using other tools

### Confirmation

Implementation will be verified through:

* Updated project templates using `uv`
* CI/CD pipeline updates to standardize on `uv`
* Team documentation and training
* Monitoring of build times and dependency resolution issues

## More Information

Special cases:

* Teams working with data science/ML projects may continue using conda if required
* Legacy projects may maintain existing tools until convenient migration points

This decision should be reviewed in 12 months to assess:

* Community adoption of `uv`
* Team feedback and pain points
* New alternatives in the Python packaging ecosystem
