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

- Culture: Fosters trust, collaboration, and shared responsibility.
- Automation: Eliminates manual and repetitive tasks, increasing speed and reliability. (e.g., Azure Pipelines, GitHub Actions)
- Measurement: Data-driven decision-making through monitoring and KPIs. (e.g., Azure Monitor, Application Insights)
- Sharing: Open communication and knowledge transfer.

> Feedback loops are essential at every stage.

Considering:

1. People, process, tools
2. Continuous delivery: frequent coding, testing, and deployment of small changes
3. Lean management: visualizing and optimizing feedback loops
4. Change control
5. Infrastructure as code (IaC): All infra (e.g., ARM Templates, Bicep, Terraform for Azure) tracked in source control

## Practices
1. Uncident command system 
2. Developers on call 
3. Public status pages 
4. Blameless postmortems 
5. Embedded teams 
6. Cloud - control infrastructure 
7. Andon Cords - someone stops the production because catch something
8. Dependency injection 
9. Blue/ Green Deployment load balancer one is live, set - system 
10. Chaos Monkey - high reliable - making caos for testing 


## Example
The car or the horse? 

Series of tools to address out needs like pipeline 
Reviewing logistic tail which is related to a cost 

A tool criteria is:
1. programmable 
2. Verifiable -> exposes what is doing 
3. Well behaved operation point of view and deploy view 

## Communication on DevOps 
1. Blameless postmortems `48 hours` everything in time line 
2. Transparent uptime: `admit failure, sound like a human, communication channel, authentic`.

  ### The westrum model 
  1. Pathological (power oriented)
  2. Bereaucratic (rule-oriented)
  2. Generative (performance oriented)

  ### Kaizen
  Change for the better.

  `gemba` (locus the real place)
  Going to the code to see `gemba`

  Focus on symptoms: `causes - effects `. People don't fail, processes do. Don't blame.


## Agile, Lean and Itope 
  ### Agile infrastructure:
  - Requirements 
  - Design
  - Implementation 
  - Verification 
  - Maintenance

  `--> Sprint 1, 2, 3 (plan, desing, buil, test, review, launch)`

A sample value stream map:

![Alt text](https://github.com/brown9804/Azure-DevOps_initial_path/blob/main/DevOps/img/DevOps/%5Bimg%5D_DevOps_sample_value_steam_map.png "A sample value stream map ")

And the Scrum life cycle:


![Alt text](https://github.com/brown9804/Azure-DevOps_initial_path/blob/main/DevOps/img/DevOps/%5Bimg%5D_DevOps_scrum_life_cycle.png "A sample value stream map ")



  `Collaborations - Increase productivity and more ideas `

  ### Lean 
  
  Systematic software:
  - Eliminate waste 
  - `muda` Work that absorb resources add no value 
  - `muri` Unreasonable work imposed on worker and machines
  - `mura` Work coming in unevenly instead of the constant or regular flow 
  - `Value stream` Value information flows with the costumers 


Important to consider lean principles:

![Alt text](https://github.com/brown9804/Azure-DevOps_initial_path/blob/main/DevOps/img/DevOps/%5Bimg%5D_DevOps_lean_principles.png "Lean Principles ")

### Itil, Itsm, Sdlc
- `itsm `--- IT service management 
- `itil ` --- IT infrastructure library 

* Information Technology Infrastructure Library (ITIL):
Provides a comprehensive process model based
the approach of designing, managing and controlling 

* IT processes. 
Government standard `ITIL.11 ` 
1. Service strategy 
2. Service design 
3. Service transition 
4. Service operation 

`2000 pages or more :)`

## CALMS
And know ...  calms with L of leans 
- Lean management 
- Amplify learning 
- Decide as late as possible 
- Decide as fast as possible 
- Empower the team 
- Build-in integrity 
- See the whole

## Prod & Stage 
| |  Important for Prod and Stage    ||  |
|---|---|---|---|
|Continuous delivery pipeline |  Version control  | Application code  | Infrastructure code |


Amazon has cloud formation and azure has azure resource manager templates and so on one model for my systems, another for os system and other applications


##  Containers 
Efficiency reasons:
- nodes 1000
- OS dependecies 
- Docker 
- Maven deb file and Docker containers 

`CMDB - Configuration Management Data Base`

Zookeeper service as a central coordinated. Combining actions like Kubernetes and Mesos. The container is basically the app configuration management:
- Chef 
- Puppet 
- Ansible 
- Salt 
- Cfengine 
- Services directory tools 
- Etcd 
- Zookeeper
- Consul


`Docker - kubernetes - mesos` 

Private container services 
- Rancher 
- Google Cloud Platform 
- Amazon web services ecs 
* Blue live 
* Green IDLE 



## CD/CI

`Continuos Deploy `  `Continous Delivery` `Continuos Integration`

1. Time to market goes down 
2. Quality increases 
3. Continuous Delivery limits your work in progress 
4. Shortens lead times for changes 
5. Improves mean time to recover


Annotations:
- Builds should pass the coffee test <5 minutes 
- Commit small bits 
- Don't leave the build broken 
- Use a trunk - bases development flow 
- No flaky tests 
- The build should return a status, a log, and an artifact 

Important:
1. Only build artifacts once
2. Should be immutable 
3. Deployment should go to a copy of the production
4. Stop deploys if a previous step fails 
5. Deployments should be idempotent 

## Cycle and Overall Cycle Time 
Types of testing 
1. Unit testing 
2. Code hygiene 
  * Liting 
  * Code formatting 
  * Banned function checks
3. Integration testing 
4. Security testing 
  * Given I have a website 
  * When I try to attack it with XSS
  * Then it should not be vulnerable  
5. TDD Test Driven Development 
  * State desired outcome as a test
  * Write code to pass the test 
  * Repeat 
6. BDD Behavior Driven Development
  * Work with stakeholders 
  * Describe business functionality 
  * Test is based on natural language 
7. ATDD Acceptance Test Driven Development 
* End user perpective 
* Use case automated testing 
* Testing is continuous during development 
8. Infrastructure testing 
9. Performance testing - types of performance 

|                           |                    Annotations |                                              |               |  
|---|---|---|---|
| Version control `GitHub` | CI systems `jenkins`  `bamboo` | Build  `make/rake`, `maven`,  `gulp`, `packer`| Test  `j unit `, ` golint / gofmt / rubocop`|

###  Integration testing 
- Robot 
- Protractor 
- Cucumber
- Selenium 
- Artifact repository 
 - Kitchen ci
 
` Performace testing apachebench, meter` ` Security testing brakeman, veracode`

Where?
- Artifactory 
- Nexus 
- Docker hub
- AWS s3


Deployment:
- Rundeck 
- Urbancode
- Thoughtworks
- Deployinator 


## Desing for operation theory 
* Circuit breaker functionality ` dm_control ` if inside 
* Design for operation practice 
* Chaos monkey --- avoid failure by making fail it 
* Cassandra 3 replicas

## Metrics and monitoring 
How complex systems fail?
* Change introduces new forms of failure 
* Complex system contain changing mixtures of failures latent within them
* All complex system is always running in degraded mode 


Lean approach:
1. Build
2. Measure 
3. Learn 
4. Repeat 

So: 
* Service performance and uptime 
* Software component metrics 
* System metrics  
* App metrics
* Performance: Linting, code formatting, banned function checks 
* Security systems 

## 5 ws of logging 
1. What happend?
2. When 
3. Where
4. Who 
5. Where did that ebtuty come from?

Remainders:
- Do not collect log data if you never plan to use it
- Retain log data for as long as it is conceivable that it can be used 
- Log all you can but alert only what you must respond to 
- Don't try to make your logging more available or more secure than your production stack
- Logs change 


## SRE tool chain 
Software as a service monitoring:
- ` Pingdom`
- ` Datadog `
- ` Netuitive `
- ` Ruxit `
- ` Librato`
- ` New relic `
- ` App dynamics `


## Open source monitoring 
* Graphite 
* Grafana 
* Statsd
* Ganglia 
* InfluxDB
* OpenTSDB
  - `prometeus `
  - ` paperduty`
  - ` flapjack `
* SAAS providers 
 

<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-1192-limegreen" alt="Total views">
  <p>Refresh Date: 2025-07-16</p>
</div>
<!-- END BADGE -->
