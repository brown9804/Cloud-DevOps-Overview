# DevOps 
----------

Costa Rica

Belinda Brown, belindabrownr04@gmail.com

Jun, 2020

----------

Has his roots in agile and iterative 

`
Code + systems 
`

## CAMS
- Culture 
- Automation
- Measurement
- Sharing

*More feedback loops

Considering:
1. People, process, tools
2. Continuous delivery coding, testing small parts
3. Lean management feedback loops, visualization
4. Change control 
5. infrastructure code - checked into source control 



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
 

