# ADR - Architecture Decision Records Naming Convention

**Status**: proposed  
**Date**: 2025-03-24  
**Governance**: Drafted for DHCW Technical Design Authority (TDA) for approval

## Situation - Context and Problem Statement

* We want to record architecture related decisions for NHS Wales organisations, made via agreed governance mechanisms. 
* We need to agree a **naming convention** for the records i.e how to name records and refer to them.
* We should also agree a **filename convention** aligned with the naming convention.

## Background - Decision Drivers
We want:
* a consistent naming convention for our decisions.
* names to be human readable and easy to understand.
* to be able to cross-reference ADRs easily.
* the naming to support multiple ADRs being developed in parallel (i.e. avoid naming clashes).

## Assessment - Considered Options

For naming itself:
* Just sequential numbering e.g. ADR 0001, ADR 0002, ...
* Sequential numbering and titles e.g. ADR 0001 - ADR-0001-Title, ADR 0002 - Title, ...
* Just titles e.g. ADR - Title, ADR - Title
* Formless – No naming convention - author's choice.

For filenames:
* The title of the ADR as above as-is e.g. ``ADR - Title Goes Here.md``
* Use of lowercase 'kebab' style for filenames e.g. ``adr-title-goes-here.md``
* Use of lowercase 'snake' style for filenames e.g. ``adr_title_goes_here.md``

## Recommendation - Decision Outcome
### Naming Convention
Adopt an ADR **naming convention** of:
* Just titles, in Title Case, prefixed by **'ADR - '**.
* Author to ensure the title makes it clear what the decision relates to.
* Author to ensure titles are human readable and unique.
* Examples:
    * 'ADR - Use Architecture Decision Records and Structure'
    * 'ADR - Architecture Decision Records Naming Convention'
    * 'ADR - Architecture Decision Record Format as Markdown'

Whilst numbering ADRs makes them easy to cross-reference, it introduces an administrative/process overhead to ensure numbers are unique and sequential and adds complexity in the ordering of ADRs, especially when multiple ADRs are in development in parallel (which gets published first, who gets the next ADR number etc.). 

Using human readable names makes them easy to refer to and talk about.

**Note:** We are referring to ADRs as '_Architecture_' decision records, not '_Architectural_' or other similar titles.

### Filenames
Given the above, apply the following convention to **filenames**: Match the Title of the ADR and remove whitespace and adopt kebab style e.g. 
* ``adr-architecture-decision-records-naming-convention.md``
* ``adr-use-architecture-decision-records-and-structure.md``
* ``adr-specify-adr-format-as-markdown.md``

### Cross Referencing
When cross-referencing ADRs, use the full title of the ADR and link to the record filename itself e.g.
* See [ADR - Architecture Decision Records Naming Convention](adr-architecture-decision-records-naming-conventions.md)

### Branches
Git branch names should utilise the same convention as the main filename of the ADR itself e.g.
* ``git checkout -m adr-architecture-decision-records-naming-convention``

### Confirmation

This ADR will be enforced by reviewers of newly submitted ADRs, who should refer to this ADR and confirm the naming convention and decision herein is being adhered to.

## More Information (Optional)
See [ADR - Use Architecture Decision Records and Structure](adr-use-architecture-decision-records-and-structure.md) for the structure of ADRs