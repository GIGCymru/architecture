# Architecture Design Overview: {Programme/Project Name}

## Document Details

**Document author**: ...

**Document version**: ...

**Status**: { Draft | Approved }

**Approved by**: ...

**Date approved**: ...

**Review date**: yyyy/mm/dd

**Template version**: 1.2

### Revision History

| Date       | Version | Author   | Revision Summary              |
| ---------- | :-----: | -------- | ----------------------------- |
| yyyy-mm-dd |  v0.1   |   ...    |            ...                |

### Approval/Scrutiny History

| Committee or Group | Date       | Outcome                     |
| ------------------ | ---------- | --------------------------- |
|        ...         | yyyy-mm-dd | {Draft / Approved / Approved with caveats / Not Approved} |

## 1. Introduction and Goals

> **Please delete guide text before submission**
>
> Describes the relevant requirements and the driving forces that software
> architects and development team must consider. These include:
>
> • Underlying business goals,
>
> • Essential features,
>
> • Essential functional requirements,
>
> • Quality goals for the architecture and
>
> • Relevant stakeholders and their expectations

...

### 1.1 Requirements Overview

...

### 1.2 Quality Goals

...

### 1.3 Stakeholders

The target audience for this design, and their interests, include:

| Role/Name | Contact     | Expectations |
| --------- | ----------- | ------------ |
|    ...    |    ...      |     ...      |

## 2. Architecture Constraints

> **Please delete guide text before submission**
>
> Any requirement that constrains software architects in their freedom of design
> and implementation decisions or decision about the development process. These
> constraints sometimes go beyond individual systems and are valid for whole
> organizations and companies.

...

## 3. Context and Scope

> **Please delete guide text before submission**  
>
> As the name suggests - delimits your system (i.e. your scope) from all its  
> communication partners (neighbouring systems and users, i.e. the context of  
> your system). It thereby specifies the external interfaces.  
>
> If necessary, differentiate the business context (domain specific inputs and  
> outputs) from the technical context (channels, protocols, hardware).

...

### 3.1 Business Context

...

### 3.2 Technical Context

...

## 4. Solution Strategy

> **Please delete guide text before submission**
>
> A short summary and explanation of the fundamental decisions and solution
> strategies, that shape system architecture. It includes:
>
> • Technology decisions
>
> • Decisions about the top-level decomposition of the system, e.g. usage of an
> architectural pattern or design pattern
>
> • Decisions on how to achieve key quality goals
>
> • Relevant organizational decisions, e.g. selecting a development process or
> delegating certain tasks to third parties.

...

## 5. Building Block View

> **Please delete guide text before submission**  
>
> The building block view shows the static decomposition of the system into  
> building blocks (modules, components, subsystems, classes, interfaces,  
> packages, libraries, frameworks, layers, partitions, tiers, functions,  
> macros, operations, data structures, ...) as well as their dependencies  
> (relationships, associations, ...)  
>
> This view is mandatory for every architecture documentation. In analogy to a  
> house this is the floor plan.

...

### 5.1 C4 Level 1 View

...

### 5.2 C4 Level 2 View

...

## 6. Runtime View

> **Please delete guide text before submission**
>
> The runtime view describes concrete behaviour and interactions of the
> system's building blocks in form of scenarios from the following areas:
>
> • Important use cases or features: how do building blocks execute them?
>
> • Interactions at critical external interfaces: how do building blocks
> cooperate with users and neighbouring systems?
>
> • Operation and administration: launch, start-up, stop
>
> • Error and exception scenarios
>
> Remark: the main criterion for the choice of possible scenarios (sequences,
> workflows) is their architectural relevance. It is not important to describe
> a large number of scenarios. You should rather document a > representative
> selection.

...

## 7. Deployment view

> **Please delete guide text before submission**
>
> The deployment view describes:
>
> • Technical infrastructure used to execute your system, with elements like
> geographical locations, environments, computers, processors, channels and net
> topologies as well as other elements and
>
> • Mapping of (software) building blocks to that infrastructure elements.
>
> Often systems are executed in different environments, e.g. development
> environment, test environment, production environment. In such cases you
> should document all relevant environments.
>
> Especially document a deployment view if your software is executed as
> distributed system with more than one computer, processor, server or
> container or when you design and construct your own hardware processors and
> chips.
>
> From a software perspective it is sufficient to capture only those elements
> of an infrastructure that are needed to show a deployment of your building
> blocks. Hardware architects can go beyond that and describe an infrastructure
> to any level of detail they need to capture.

...

## 8. Crosscutting Concepts

> **Please delete guide text before submission**
>
> This section describes overall, principal regulations and solution ideas that
> are relevant in multiple parts (= cross-cutting) of your system. Such
> concepts are often related to multiple building blocks. They can include
> many different topics, such as
>
> • Models, especially domain models
>
> • Architecture or design patterns
>
> • Rules for using specific technology
>
> • Principal, often technical decisions of an overarching (= cross-cutting)
> nature
>
> • Implementation rules

...

### 8.1 Design Patterns

...

### 8.2 Security

...

### 8.3 Scalability

...

### 8.4 Resilience

...

### 8.5 Observability

...

### 8.6 Regulatory & Compliance

...

## 9. Architecture Decisions

> **Please delete guide text before submission**
>
> Important, expensive, large scale or risky architecture decisions including
> rationales. With "decisions" we mean selecting one alternative based on given
> criteria.
>
> Please use your judgement to decide whether an architectural decision should
> be documented here in this central section or whether you better document it
> locally (e.g. within the white box template of one building block).
>
> Avoid redundancy. Refer to section 4, where you already captured the most
> important decisions of your architecture.

...

### 9.1 New ADRs

| ID    | Impact              |
| ----- | ------------------- |
| ##### |        ...          |

### 9.2 Design History

| Date       | Impact              | Rationale       |
| ---------- | ------------------- | --------------- |
| yyyy-mm-dd |         ...         |      ...        |

## 10. Quality Requirements

> **Please delete guide text before submission**  
>
> This section contains all quality requirements as quality tree with scenarios.  
> The most important ones have already been described in section 1.2. (quality  
> goals)  
>
> Here you can also capture quality requirements with lesser priority, which  
> will not create high risks when they are not fully achieved.

...

## 11. Risks and Technical Debt

> **Please delete guide text before submission**  
>
> As the name suggests - delimits your system (i.e. your scope) from all its  
> communication partners (neighbouring systems and users, i.e. the context of  
> your system). It thereby specifies the external interfaces.  
>
> If necessary, differentiate the business context (domain specific inputs and  
> outputs) from the technical context (channels, protocols, hardware).

### 11.1 Risks

| ID   | Impact                | Mitigation / Plan | Owner          |
| ---- | --------------------- | ----------------- | -------------- |
| #### | {Low / Medium / High} |       ...         |       ...      |

### 11.2 Technical Debt

| ID   | Impact                | Mitigation / Plan | Owner          |
| ---- | --------------------- | ----------------- | -------------- |
| #### | {Low / Medium / High} |       ...         |       ...      |

## 12. Glossary

| Term         | Definition            |
| ------------ | --------------------- |
|     ...      |         ...           |
