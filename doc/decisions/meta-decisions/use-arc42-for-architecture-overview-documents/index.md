# Adoption of Architecture Overview Documents

**Status**: Proposed

**Level**: 3

**Updated**: 2025-07-24

## Situation: Context and Problem Statement

DHCW has well-established assurance processes for design that have been aligned to traditional waterfall methodologies for many years. As part of this approach, architects complete designs documented in Solution Architecture Documents (SADs), which are then peer-reviewed by the TDAG committee comprising experts from all major technical domains.

There are several issues associated to using SADs within the organisation:

* SADs reflect the initial design from an architectural perspective, but they do not reflect what gets implemented.
* SADs tend to be very lengthy documents and are difficult to consume for the end reviewers.
* SAD format doesn't take into account all areas of design concern.

## Background: Decision Drivers

The current assurance process results in SADs that often become obsolete once services are delivered, as changes made during implementation are not consistently captured or updated. This leads to a loss of accuracy in the documented state of the global architecture, reducing confidence in SADs as a reliable source of truth.  Decision drivers are as follows:

* Modern ways of working need to focus on iterative approaches to design.
* Design assurance is needed earlier and iteratively.
* Architecture needs to be a continuous activity, and documentation needs to reflect that.
* Architects are no longer singularly responsible for updating designs, and collaboration between disciplines to maintain the documentation is needed.
* Focus on end-to-end design architecture, rather than just software.
* Adopt a template format that AI can interpret and work with to improve their output when asked to contribute to projects.

## Assessment: Considered Options

Several options were identified that could be considered for the review:

**1. Keep existing documentation standards(Keep SAD, SRS, HLD, LLD)** - this approach no longer fits and is sustainable for the change to Product focussed delivery.

**2. Come up with a DHCW specific lightweight design template.** - A lightweight format can be adopted but will require DHCW to agree a format, and manage the document format as a product.

**3. Adopt a supported recognised industry standard.** - Best of both worlds.  A lightweight format that can be adopted in line with other new tools, and maintained by the industry keeping it relevant to the latest architecture concerns.

**Option 3** was investigated in further detail to identify possible options.  The following options were considered:

* **C4 modelling** - excellent tool for modelling software, however lacking the end-to-end view.

* **Arc42** - An industry wide adopted methodology for documenting architecture, open source and supported, primarily based on Markdown.  Well documented template in multiple formats, with supporting documentation to assist architects through the information gathering process.  Many supporting examples.

## Recommendation: Decision Outcome

After consideration, the decision is that DHCW will adopt the arc42 modelling template for solution architecture for the following reasons:

**1. Structured and Comprehensive Framework** - arc42 provides a well-defined, standardised template covering all critical aspects of architecture, including context, constraints, quality scenarios, building blocks, runtime views, and decisions. This ensures designs are documented holistically rather than inconsistently or partially, which is common with unstructured documentation.

**2. Decision-Centric and Maintainable** - It integrates architectural decisions (via ADRs) directly within the design structure, promoting traceability of why choices were made. This is more maintainable than freeform documents like traditional SADs, which often focus only on static design outputs rather than design rationale.

**3. Technology-Agnostic and Methodology-Neutral** - arc42 does not enforce any specific technology stack or delivery methodology (waterfall, agile, or hybrid). Its adaptability makes it ideal in mixed delivery environments like DHCW, where multiple approaches coexist.

**4. Widely Adopted and Supported** - It is an internationally recognised and peer-reviewed framework used across industries, with extensive guidance, examples, and community support. This ensures new team members can onboard quickly and understand documentation without bespoke organisational training.

**5. Promotes Consistency and Reuse** - By enforcing a common structure and language across projects and teams, arc42 reduces cognitive load, facilitates reviews and assurance processes (such as TDAG), and enables reuse of design knowledge across programmes, improving architectural governance maturity.

**6. Optimised for AI Interpretation and Generation** - The structured and consistent nature of the arc42 template makes it highly suitable for AI tools to interpret, generate, or update documentation efficiently. Its clear separation of concerns and predictable sectioning allow AI assistants to analyse, summarise, validate, or even draft architecture content with minimal ambiguity, enhancing productivity and ensuring documentation remains up to date.

For more information on arc42, go to [arc42.org](https://arc42.org/)
