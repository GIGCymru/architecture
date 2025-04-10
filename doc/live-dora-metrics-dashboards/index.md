# Live DORA Metrics Dashboards

!!! note
    Work in Progress

**Status**: first sketch, work in progress, request for collaboration

**Date**: Updated 2025-04-08

**Governance**: To Be Discovered; potentially a combo of this repo participants, DHCW CISO, NHS Wales UCB peers, etc.

## Context

Broadly, our organization wants to improve the quality of our software
engineering, and we want to do this by making software engineering metrics
visible. We intend to start with the DevOps Research and Assessment (DORA)
report because these are well-known, well-understood, and well-researched.

### What are DORA Metrics?

<https://dora.dev/guides/dora-metrics-four-keys/>

The DORA metics are:

* Lead Time - This metric measures the time it takes for a code commit or change
  to be successfully deployed to production. It reflects the efficiency of your
  software delivery process.

* Deployment Frequency - This metric measures how often application changes are
  deployed to production. Higher deployment frequency indicates a more efficient
  and responsive delivery process.

* Change Failure - This metric measures the percentage of deployments that cause
  failures in production, requiring hotfixes or rollbacks. A lower change
  failure rate indicates a more reliable delivery process.

* Recovery Time a.k.a. Time to Restore Service a.k.a. Failed Deployment Reset
  Time - This metric measures the time it takes to recover from a failed
  deployment. A lower recovery time indicates a more resilient and responsive
  system.

These metrics are in two categories:

* Throughput: Lead Time & Deployment Frequency.

* Stability: Change Failure & Recovery Time.

## Drivers

We want to develop a live dashboard to track our projects' DORA metrics. This
dashboard will be used by software engineering teams, including our programmers,
project managers, and all the project's other stakeholders.

We believe this kind of visibility, transparency, and monitoring can help us
improve our software engineering practices and outcomes.

We believe the live DORA metrics dashboards will likely include the kinds of
aspects below.

**Data Sources**:

* **Git/CI/CD System** to retrieve lead time, deployment frequency, change
  failure rate, and recovery time.

* **Incident Management Tools** to help calculate the time to restore service.

**Data Collection and ETL Process**:

* **ETL (Extract, Transform, Load)** pipelines to gather data from the above
  systems, across projects, then aggregate it into a central data store.

* Data will be refreshed at regular intervals (e.g., every hour) to provide
  usable daily-quality metrics.

* The collected data will be stored in a data store TBD. We may want to try a
  Time-series Database (TSDB) rather than a relational database (RDB) because
  time-series data may provide efficient querying and retrieval of time-based
  metrics.

**Backend Services**:

* A RESTful API will serve as the backend for the dashboard, handling
  requests from the frontend.

* Authentication and authorization TBD.

**Frontend (Dashboard)**:

* The dashboard will be built using JavaScript/TypeScript for flexibility and
  maintainability.

* Data visualization will be handled using an off-the-shelf charting library TBD.

* We'll consider developing the frontend to update dynamically based on data
  changes via WebSockets or Server-Sent Events (SSE).

**Monitoring and Alerts**:

* We may want to create alerts. For example, we may want to create alerts that
  will be triggered when certain thresholds are exceeded (e.g., high failure
  rate, slow recovery time). These alerts will be visible in the dashboard and
  could also be pushed to our messaging system.

* We will also monitor the health of the dashboard itself.

## Alternatives Considered

**Manual data collection vs. automated ETL pipelines**:

* Initially, we considered manually extracting metrics through scheduled
  scripts, but this would be error-prone and less maintainable. The automated
  ETL pipelines were chosen for their scalability and reliability.

**Using a traditional relational database vs. time-series database**:

* We considered using a relational database (e.g., PostgreSQL) to store DORA
  metrics, but time-series databases like **InfluxDB** offer optimized storage
  and query performance for time-based data, making them a better choice for
  this use case.

***Frontend technologies**:

* We evaluated using **Vue.js** or **Angular** for the frontend but decided on
  **React.js** due to its widespread adoption, large community, and extensive
  library support for real-time data visualization.

## Common pitfalls

From <https://dora.dev/guides/dora-metrics-four-keys/>

There are some pitfalls to watch out for as your team adopts DORA’s software delivery metrics, including the following:

* Setting metrics as a goal. Ignoring Goodhart’s law and making broad statements
  like, “Every application must deploy multiple times per day by year’s end,”
  increases the likelihood that teams will try to game the metrics.

* Having one metric to rule them all. Attempting to measure complex systems with
  the idea that only one metric matters. Teams should identify multiple metrics,
  including some with a healthy amount of tension between them. The SPACE
  framework can guide your discovery of a set of metrics.

* Using industry as a shield against improving. For example, some teams in
  highly regulated industries might claim that compliance requirements prevent
  them from disrupting the status quo.

* Making disparate comparisons. These metrics are meant to be applied at the
  application or service level. Comparing metrics between vastly different
  applications (for example, a mobile app and a mainframe system) can be
  misleading.

* Having siloed ownership. Sharing all four metrics across development,
  operations, and release teams fosters collaboration and shared ownership of
  the delivery process. Isolating teams with specific metrics can lead to
  friction and finger-pointing.

* Competing. The goal is to improve your team’s performance over time, not to
  compete against other teams or organizations. Use the metrics as a guide for
  identifying areas for growth and celebrating progress.

* Focusing on measurement at the expense of improvement. The data your team
  needs to collect for the four keys is available in a number of different
  places today. Building integrations to multiple systems to get precise data
  about your software delivery performance might not be worth the initial
  investment. Instead, it might be better to start with having conversations,
  taking the DORA Quick Check, or using a source-available or commercial product
  that comes with pre-built integrations.

## Consequences

**Maintenance**: The dashboard will require ongoing maintenance, especially with
regards to data source integrations and ensuring the ETL pipelines are
functioning properly.

## Next Steps

We believe we should gather information about two kinds of approaches:

1. Build: We can build the dashboard from scratch.

2. Buy: We can purchase a commercial dashboard solution.

If we choose to build, then we believe the steps would be:

1. **Build the frontend dashboard** with real-time visualizations of test metrics.

2. **Develop the RESTful API** to serve data to the frontend.

3. **Implement the ETL pipelines** for collecting data from the various sources.

4. **Deploy the system** by using CI/CD and ideally targeting a public cloud.

## Recommendation - Decision Outcome

TODO
