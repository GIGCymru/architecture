# Software design development guidance

!!! note
    Work in Progress

**Status**: first sketch, work in progress, request for collaboration

**Date**: 2025-03-31

**Governance**: To Be Discovered; potentially a combo of this repo partipants, DHCW CISO, NHS Wales UCB peers, etc.

## Situation - Context and Problem Statement

Broadly we need to design and develop many software products for patients and healthcare workers, and we want our design and development to emphasize usability, accessibility, maintainability, and similar system quality attributes.

Narrowly we need to immediately design and develop the emergency department module, and we need to give the program some UI/UX guardrails:

* Design system: e.g. how should a top navigation menu look and feel to the user.
  
* Development system: e.g. how should a programmer implement the menu with JavaScript/TypeScript.
 
* Testing system: e.g. how to test the menu for accessibility, multi-language capability, etc.

## Background - Decision Drivers

We want to get good-enough quality work in place now, so we can try it out, ask for feedback, and seek help from peers and advisors.

We want to align with existing design-development recommends, not reinvent the wheel.

We generally favor considering systems that we are confident are relevant and ready:

* Government guidelines: GOV.UK Design System, NHS.UK Design System, 18F Design System, others?

* Business specifications: Apple Human Interfaces Guidelines, Google Material Design, Microsoft Fluent Design System, others?

* Free open source components using JavaScript and TypeScript: shadcn, Flowbite, SkeletonUI, others?

## Assessment - Considered Options

We generally favor considering systems that we are confident are relevant and ready:

### Government guideline: GOV.UK Design System

[GOV.UK Design System](https://design-system.service.gov.uk/)

TODO

### Government guideline: NHS.UK Design System

[NHS.UK: Design system](https://service-manual.nhs.uk/design-system)

TODO

### Government guideline: 18F Design System

[18F.gov: The U.S. Web Design System ](https://guides.18f.gov/ux-guide/design/use-a-design-system/)

TODO

### Business specifications: Apple Human Interfaces Guidelines

[Apple Human Interface Guidelines (HIG)](https://developer.apple.com/design/human-interface-guidelines)

TODO

### Business specifications: Google Material Design

[Google Material Design 3](https://m3.material.io/)

TODO

### Business specifications: Microsoft Fluent Design System

[Microsoft Fluent 2 Design System](https://fluent2.microsoft.design/)

TODO

### Component framework: shadcn

[shadch: build your component library](https://ui.shadcn.com/)

TODO

### Component framework: Flowbite

[Flowbite: Build websites even faster with components])https://flowbite.com/)

TODO

### Component framework: SkeletonUI

[SkeletonUI adaptive design system](https://www.skeleton.dev/)

TODO


## Recommendation - Decision Outcome

Given what we know so far, and the immediacy of the emergency department module, we are immediately pursuing the combination of one choice in each category that we believe will keep the most options open for our ongoing improvements and learning. In other words, we need to kickstart real work, and we know that what we learn about our needs may well alter our longer-term choices.

* Government guidelines: We are kickstarting with GOV.UK because these guidelines are good enough for now, and definitely intended for all of the UK (including Wales), and we don't need to cut out anything that NHS England might have added that's specific to England.

* Business specifications: We are kickstarting with Apple Human Interface Guidelines: because these orient more toward high-level principles (especially usability and accessibility), rather than low-level rendering (such as colors, fonts, grids).

* Component framework: We are kickstarting shadcn because it is free open source, widespread worldwide, has implementations in JavaScript and TypeScript, and has multiple tunings for specific development frameworks, which in turn improves maintainability and testability.

Ways of working:

* We start now, and we do continuous improvement as we learn more about the real work.

* We understand that all of these options are significantly ahead of NHS Wales DHCW can design and develop internally, because we are resourced constrained.

* We believe that any combination of the above options will be better than none, so we're using the principles of 1) bias for action, 2) don't let perfect be the enemy of the good, 3) ship soon then improve, 4) helping the emergency department staff and getting their direct feedback is a higher priority than any specific pre-planning of colors, fonts, logos, layouts, etc.
