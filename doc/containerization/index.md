# Containerization

!!! note
    Work in Progress

**Status**: first sketch, work in progress, request for collaboration

**Date**: 2025-04-17

**Governance**: To Be Discovered; potentially a combo of this repo participants, DHCW CISO, NHS Wales UCB peers, etc.

## Situation - Context and Problem Statement

To support our software engineering teams with reliable, portable, and secure
environments for application development, testing, and deployment, we need a
consistent approach to containerization, container management, and container
deployment.

Right now we need:

* Capabilities for software engineers to develop software locally in a container.

* Capabilities for software engineers to download and run software in containers.

Broadly we want to aim for:

* Support for **infrastructure-as-code** and CI/CD pipelines.

* Demand for **rootless** and secure containers (developer-friendly, production-safe).

* Consideration for **direct vs. orchestrated** container management.

* Growing interest in **serverless runtimes** and integration with ephemeral compute.

We must decide on:

* Container engine(s) to use (such as Docker, Podman, etc.)

* How we build, run, and manage containers (locally, in CI/CD/CT, in demos, in production, etc).

* Deployment methods (manual, automated, orchestrated, serverless, etc).

## Drivers

* **Compatibility:** Must work well with Git/GitHub, Tofu/Terraform, CI/CD/CT pipelines.

* **Portability:** Support across developer machines and CI environments.

* **Flexibility:** Support serverless where appropriate.

* **Security:** Rootless containers reduce the attack surface.

* **Simplicity:** Avoid Kubernetes unless orchestration is absolutely required.

## Considered Options

* Docker

* Podman

* Serverless e.g. closed-source platform-specific such as AWS Fargate Serverless Compute, open-source platform-agnostic such as Knative

* Direct management (e.g., via systemd or scripts)

* Kubernetes / Orchestration tools

## Evaluation

### Docker

Pros:

* Ubiquity

* Wide ecosystem

* Docker Compose is very handy.

Cons:

* Requires daemon

* Default setup needs root access unless configured

* Licensing shenanigans

### Podman

Pros:

* Rootless

* Daemonless

* OCI-compatible

* Docker CLI compatible

Cons:

* Some ecosystem gaps

* Fewer tutorials and LLM prompts

### Serverless (Lambda, Knative)

Pros:

* Auto-scaling

* No infra to manage.

Cons:

* Cold start latency

* Limited runtime control

* Vendor-specific setup doesn't lend itself to multi-cloud resilience

* No overlap with local tooling


### Direct management (e.g., via systemd or scripts)

Pros:

* Lightweight, fast, easy

* Excellent for local software engineering

Cons:

* Lacks orchestration

* Not scalable

* Not easy in the cloud


### Kubernetes / Orchestration tools

Pros:

* By far the most powerful, scalable, and capable, for professional operations teams

* Definitely where we want to be aiming in the next couple of years

Cons:

* Complex - probably too complex to ask mid-level software engineers to pick up for a non-ops project

* Overhead - probably too big a lift right now for us, because we don't have the networking setups

## Implications

* Software engineering developer environments should transition to containers where feasible.

* CI/CD/CT pipelines will include container build steps with containers, depending on runner environment.

* Documentation and training needs to be created for software engineers to learn about containerization.

* For more-complex deployment needs, we'll need to create a path for
  containerization leading to eventual use of Kubernetes or serverless platforms
  depending on cost/performance trade-offs.

## References

* [Podman Documentation](https://podman.io)

* [Docker Documentation](https://docs.docker.com)

* [Open Container Initiative (OCI)](https://opencontainers.org/)

* [AWS Lambda Container Support](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html)

## Decision

We will adopt the following containerization and management strategy:

Container Engine:

* Use **Podman** as the default engine for local development and rootless use cases.

* Support **Docker** where Podman isn't viable, such as a project already using Docker Compose.

Container Image Management:

* Use **OCI-compliant** image builds.

* Store and retrieve images via internal and external registries (e.g., ECR, Docker Hub, GitHub Container Registry).

Execution and Management:

* For local development: encourage **Podman rootless** containers to increase security and reduce dependency on Docker daemon.

* For CI/CD/CT: Use **containerized runners** (e.g., GitHub Actions, GitLab Runners) with Podman setups depending on environment support.

* For ephemeral execution: leverage serverless runtimes when the workload fits.

Infrastructure as Code Integration:

* Container lifecycle (build, deploy, destroy) will be managed through IaC tools such as Tofu/Terraform, or similar complementary technologies such as Dagger, Pulumi or Ansible. We intend to do a complementary ADR for these.

* All container-related infra should be declarative and version-controlled.
