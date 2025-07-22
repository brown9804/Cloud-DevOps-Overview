# DevOps Overview

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2025-07-11

----------

> DevOps is rooted in agile and iterative methodologies, bridging the gap between development (code) and operations (systems). It emphasizes collaboration, automation, and continuous improvement to deliver value quickly and reliably.

`DevOps = Code + Systems + Culture`


<details>
<summary><b>List of References </b> (Click to expand)</summary>

- [DevOps Foundations](https://www.linkedin.com/learning/devops-foundations/development-and-operations-2?u=2095204)
- [Agile Software Development: Kanban for Developers](https://www.linkedin.com/learning/agile-software-development-kanban-for-developers/putting-kanban-to-work-in-your-development-team?u=2095204)
- [DevOps Foundations: Lean and Agile](https://www.linkedin.com/learning/devops-foundations-lean-and-agile/lean-and-agile-in-devops-3?u=2095204)
- [Agile Software Development: Scrum for Developers](https://www.linkedin.com/learning/agile-software-development-scrum-for-developers/scrum-for-agile-software-development?u=2095204)
- [Transitioning from Waterfall to Agile Project Management](https://www.linkedin.com/learning/transitioning-from-waterfall-to-agile-project-management-2019/build-a-successful-transition-to-agile?u=2095204)
- Azure DevOps - [How to create a Azure Devops Story Template](https://docs.microsoft.com/en-us/azure/devops/boards/backlogs/work-item-template?view=azure-devops&tabs=browser)
- Azure DevOps - [How to leave from a Azure DevOps Organization](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/faq-user-and-permissions-management?view=azure-devops)
- Azure DevOps - [Create Release Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/release/triggers?view=azure-devops#continuous-deployment-triggers)
- Project Management - [What are Functional and Non-Functional Requirements and How to Document These](https://enkonix.com/blog/functional-requirements-vs-non-functional/)
- GitHub - [Building and testing Python](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python), for more information about how to run it on PR [click here](https://futurestud.io/tutorials/github-actions-run-on-pull-request#:~:text=but%20Not%20Both-,Run%20Actions%20on%20Pull%20Requests,%5D%20and%20you're%20done.)
- For the CI part, it's related to the `yml` file, find an example [here](https://github.com/brown9804/SDLC-Cloud_Lpath/blob/main/Cloud/3-automation_principles/1_api_automations/3_countryinfo_travellers/azure-pipelines.yml)
- For the CD part, we can use Azure DevOps pipelines, find [here](https://learn.microsoft.com/en-us/azure/devops/pipelines/create-first-pipeline?view=azure-devops&tabs=java%2Cbrowser) a guide.
- [How to automate the testing](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python#testing-your-code), and [Running python tests on GitHub](https://thiagolopessilva.medium.com/running-unit-testing-on-github-action-using-pytest-61653d993c9c) using github actions

</details>

## Overview 

- [Example of CI](https://github.com/brown9804/SDLC-Cloud_Lpath/blob/main/Cloud/3-automation_principles/1_api_automations/3_countryinfo_travellers/azure-pipelines.yml)
- [Example of Automated Testing](https://github.com/brown9804/SDLC-Cloud_Lpath/blob/main/.github/workflows/automated_testing.yml)
- [Example of Integrated Testing](https://github.com/brown9804/SDLC-Cloud_Lpath/blob/main/Cloud/3-automation_principles/1_api_automations/3_countryinfo_travellers/tests/shared_tests.py)

    <img width="800" alt="image" src="https://github.com/brown9804/SDLC-Cloud_Lpath/assets/24630902/4d320096-70de-4091-8505-281c19ff71eb">

## CAMS

> The CAMS framework underpins DevOps culture:

- **Culture:** Fosters trust, collaboration, and shared responsibility across development and operations. Azure Boards and Azure DevOps Teams help build this culture by enabling transparent work tracking, communication, and shared goals.
- **Automation:** Eliminates manual and repetitive tasks, increasing speed and reliability. Azure Pipelines automates build, test, and deployment processes for almost any platform or language, integrating seamlessly with GitHub, Azure Repos, and external systems.
- **Measurement:** Data-driven decision-making through monitoring and KPIs. Azure Monitor and Application Insights provide full-stack observability, helping teams make informed decisions, detect regressions, and optimize performance.
- **Sharing:** Open communication and knowledge transfer is critical for continuous improvement. Azure DevOps Wikis, dashboards, and integrated documentation ensure knowledge is captured and shared.

> Feedback loops are essential at every stage, ensuring rapid learning and improvement.

Consider:

1. **People, process, tools:** Align all three for success.
2. **Continuous delivery:** Frequently code, test, and deploy small changes. Azure DevOps supports this with pipelines, environments, and approvals.
3. **Lean management:** Use Azure Boards for visualizing and optimizing feedback loops (Kanban, Scrum).
4. **Change control:** Azure DevOps tracks every change, from code to infrastructure, with audit trails and permissions.
5. **Infrastructure as Code (IaC):** Use ARM Templates, Bicep, or Terraform (with Azure provider) to manage all infrastructure as version-controlled code.
   
## Practices

1. **Incident Command System:** Clear escalation processes and command structures. Azure Monitor can automate incident creation and notifications.
2. **Developers On Call:** Developers participate in on-call rotations to increase ownership and system reliability. Azure Alerts can route issues to the right engineer.
3. **Public Status Pages:** Use Azure Service Health and/or third-party integrations for transparency on outages and maintenance.
4. **Blameless Postmortems:** Review incidents to learn and improve, not to blame. Document lessons and action items in Azure Boards.
5. **Embedded Teams:** Cross-functional teams own products end-to-end, reducing silos.
6. **Cloud Infrastructure Control:** Use Azure Resource Manager (ARM) for fine-grained, auditable control.
7. **Andon Cords:** Any team member can stop a deployment to fix critical issues, using pipeline approvals or manual interventions in Azure Pipelines.
8. **Dependency Injection:** Design applications for loose coupling and testability, supported by Azure Functions and microservices patterns.
9. **Blue/Green Deployments:** Use Azure Traffic Manager or Azure Front Door to route traffic between live and staging environments for safe rollouts.
10. **Chaos Engineering:** Use Azure Chaos Studio to deliberately inject failures and validate system resilience.

## Example

> The car or the horse?  
- Tooling should fit the problem and context, whether it's a simple script or an advanced Azure DevOps pipeline.  
- Reviewing the logistics tail (cost, complexity) is critical when choosing DevOps tools.

**Tool Criteria:**

1. **Programmable:** Can it be automated through APIs or scripts? Azure offers comprehensive REST APIs and CLI tools.
2. **Verifiable:** Does it expose logs, events, and metrics for audit and troubleshooting? Azure Activity Log and Monitor support this.
3. **Well-behaved (Ops and Deploy View):** Is it reliable, observable, and easy to deploy/manage at scale? Azure services are designed with these principles by default.


## Communication on DevOps 

1. **Blameless Postmortems:** Conduct within 48 hours, use clear timelines, and focus on processes. Azure Boards can be used to track actions and share outcomes.
2. **Transparent Uptime:** Admit failure, communicate in human language, and use authentic channels (e.g., Azure Service Health, Teams integration).

### The Westrum Model 

1. **Pathological:** Power-oriented, suppresses information.
2. **Bureaucratic:** Rule-oriented, risk-averse.
3. **Generative:** Performance-oriented, values learning and innovation. This is the DevOps target culture.

### Kaizen

> Continuous improvement: make small, regular changes for the better.

**Gemba:** "Go to the real place": visit the code, the infrastructure, and observe reality directly to find root causes.

**Focus on symptoms:** Address process failures, not personal blame.

## Agile, Lean and IT Operations

### Agile Infrastructure

> Agile sprints (plan, design, build, test, review, launch) can be applied to infrastructure as well as code, using Azure Boards for agile tracking and Azure Pipelines for automation.

- Requirements
- Design
- Implementation
- Verification
- Maintenance

> A sample value stream map:

![Alt text](https://github.com/brown9804/Azure-DevOps_initial_path/blob/main/DevOps/img/DevOps/%5Bimg%5D_DevOps_sample_value_steam_map.png "A sample value stream map ")

> And the Scrum life cycle:

![Alt text](https://github.com/brown9804/Azure-DevOps_initial_path/blob/main/DevOps/img/DevOps/%5Bimg%5D_DevOps_scrum_life_cycle.png "A sample value stream map ")

> **Collaboration** increases productivity and brings more innovation.

### Lean 

> Lean software delivery emphasizes:

- **Eliminate Waste:** Remove non-value-adding activities.
- **Muda:** Wasteful work that absorbs resources but adds no value.
- **Muri:** Overburdening people or systems.
- **Mura:** Uneven workloads, causing bottlenecks.
- **Value Stream:** Optimize the flow of value to the customer. Azure DevOps value stream mapping helps visualize this.

Lean principles diagram:

![Alt text](https://github.com/brown9804/Azure-DevOps_initial_path/blob/main/DevOps/img/DevOps/%5Bimg%5D_DevOps_lean_principles.png "Lean Principles ")


### ITIL, ITSM, SDLC

- **ITSM:** IT Service Management: delivering value through managed IT services. Azure integrates with ITSM tools for service desk automation and incident management.
- **ITIL:** A framework for IT service delivery, including service strategy, design, transition, and operation. Azure Blueprints and Policy help enforce ITIL-aligned governance across cloud resources.
- **SDLC:** Software Development Lifecycle: the process of planning, creating, testing, and deploying information systems.

## CALMS

> CALMS builds on CAMS with a focus on Lean management:

- **Lean management:** Optimize every process, minimize waste, and maximize value.
- **Amplify Learning:** Encourage experimentation and knowledge sharing.
- **Decide as Late as Possible:** Keep options open and avoid premature decisions.
- **Decide as Fast as Possible:** Use automation and feedback to accelerate decisions.
- **Empower the Team:** Give teams autonomy and the tools to act.
- **Build-in Integrity:** Embed quality and security controls throughout.
- **See the Whole:** Understand and optimize the entire system, not just parts.

## Prod & Stage 

| Continuous delivery pipeline | Version control | Application code | Infrastructure code |
|-----------------------------|----------------|------------------|---------------------|

> Azure leverages Resource Groups, dedicated environments, and automated pipelines for strict separation and governance between production and staging.  
Amazon uses CloudFormation, Azure uses ARM Templates/Bicep for IaC, ensuring consistent cloud environments.

## Containers

> Containers provide efficiency, scalability, and portability for cloud-native workloads.

- Azure Kubernetes Service (AKS) provides managed Kubernetes clusters for orchestrating containers at scale.
- Azure Container Registry stores container images securely.
- Use Docker for local development and to package applications for cloud deployment.
- Azure supports all major configuration management and orchestration tools: Chef, Puppet, Ansible, Salt, etc.
- Service discovery in AKS is handled via built-in Kubernetes DNS or Azure DNS.

> **Private container services:** Azure Container Instances, Azure Container Apps, and private registries.

## CD/CI

**Continuous Deployment (CD), Continuous Delivery (CD), and Continuous Integration (CI):**

- Reduce time to market, improve quality, and limit work-in-progress.
- Azure Pipelines supports automated build, test, and deploy for any application or platform.
- Key principles:
    - Build processes should be fast (<5 min)
    - Commit and test small batches
    - Keep main branch always deployable
    - Use trunk-based development
    - Eliminate flaky tests
    - Build once, deploy immutably to all environments

**Immutability and idempotency:** Deployments should never rely on manual steps and must be repeatable.

## Cycle and Overall Cycle Time 

**Types of Testing:**
1. Unit testing
2. Code hygiene (linting, formatting, banned function checks)
3. Integration testing
4. Security testing (e.g., Azure Security Center, Defender for Cloud)
5. Test Driven Development (TDD)
6. Behavior Driven Development (BDD)
7. Acceptance Test Driven Development (ATDD)
8. Infrastructure testing (ensure IaC deploys as expected)
9. Performance testing (Azure Load Testing, JMeter)

| Version control `GitHub/Azure Repos` | CI/CD systems `Azure Pipelines/Jenkins` | Build tools `Make/Maven` | Test tools `JUnit/pytest/Selenium/Azure Test Plans` |

**Integration Testing:**  
Use frameworks like Robot, Selenium, Protractor, and Cucumber. Store test artifacts and results in Azure DevOps or artifact repositories.

- Performance testing: Apache Bench, Azure Load Testing.
- Security testing: Brakeman, Veracode, integrated with Azure DevOps.

Artifact repositories: Azure Artifacts, Nexus, Docker Hub, AWS S3.

Deployment automation: Azure Pipelines, Rundeck, Octopus Deploy.

## Design for Operation Theory 

- **Circuit Breakers:** Implement resilience patterns (e.g., Polly in .NET) for robust cloud applications.
- **Chaos Engineering:** Use Azure Chaos Studio to proactively test for failures and validate recovery strategies.
- **High Availability:** Design with redundancy (e.g., Cassandra 3 replicas, SQL Always On, AKS node pools).

## Metrics and Monitoring 

Understanding failure in complex systems is critical:

- Changes introduce new types of failure.
- Complex systems always contain latent failures.
- All complex systems operate in some degraded mode.

**Lean Feedback Cycle:** Build -> Measure -> Learn -> Repeat

Azure Monitor, Application Insights, and Log Analytics provide a unified platform for:

- Service reliability and uptime monitoring
- Application, system, and infrastructure metrics
- Alerting and automated remediation
- End-to-end distributed tracing

## 5 Ws of Logging 

1. What happened?
2. When?
3. Where?
4. Who?
5. Where did the event come from?

**Best Practices:**

- Log only what you need for audit, compliance, and troubleshooting.
- Retain logs for as long as they have value.
- Alert only on actionable events.
- Ensure logging is as reliable and secure as your production stack.
- Use Azure Log Analytics for querying and correlating logs.

## SRE Tool Chain 

**Software as a Service (SaaS) Monitoring:**

- Pingdom
- Datadog
- Netuitive
- Ruxit
- Librato
- New Relic
- AppDynamics

Azure-native monitoring: Azure Monitor, Application Insights.

## Open Source Monitoring 

- Graphite
- Grafana (can be connected to Azure Monitor)
- Statsd
- Ganglia
- InfluxDB
- OpenTSDB
- Prometheus (Azure Monitor supports Prometheus scraping)
- PagerDuty, Flapjack for alerting

<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-1276-limegreen" alt="Total views">
  <p>Refresh Date: 2025-07-22</p>
</div>
<!-- END BADGE -->
