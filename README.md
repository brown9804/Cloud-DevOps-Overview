# Cloud DevOps: <br> Learning Path - Overview

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2025-07-14

----------

> Provides the essential knowledge required to work effectively within Azure and embrace DevOps/Agile methodologies. Additionally, it offers insights into fundamental cloud concepts. 

<details>
<summary><b>Table of Contents</b> (Click to expand)</summary>

- [Agile](./Agile)
- [DevOps](./DevOps)
- [Network](./Network)
- [GitHub](./GitHub)
- [Cloud Principles](./Cloud)
  - [0. Linux](./Cloud/0-linux)
    - [Working with Users and Permissions](./Cloud/0-linux/lab0)
    - [System Service Management, Runlevels and Boot Targets](./Cloud/0-linux/lab1)
    - [Securely Accessing Your System](./Cloud/0-linux/lab2)
    - [Package Management and Troubleshooting](./Cloud/0-linux/lab3)
    - [File Management, Permissions and Backup](./Cloud/0-linux/lab4)
    - [Working with Text Files and Streams](./Cloud/0-linux/lab5)
    - [Linux Device Management](./Cloud/0-linux/lab6)
    - [The Linux Shell](./Cloud/0-linux/lab7)
    - [Networking](./Cloud/0-linux/lab8)
    - [Processes Management](./Cloud/0-linux/lab9)
  - [1. Terraform](./Cloud/1-terraform)
    - [Installing Terraform and Working with Terraform Providers](./Cloud/1-terraform/lab0)
    - [Using Terraform CLI Commands (workspace and state) to Manipulate a Terraform Deployment](./Cloud/1-terraform/lab1)
    - [Building and Testing a Basic Terraform Module](./Cloud/1-terraform/lab2)
    - [Exploring Terraform State Functionality](./Cloud/1-terraform/lab3)
    - [Deploy an Azure Storage Account with Terraform](./Cloud/1-terraform/lab4)
    - [Deploy an Azure File Share and Blob Storage with Terraform](./Cloud/1-terraform/lab5)
    - [Deploy Azure VNETs and Subnets with Terraform](./Cloud/1-terraform/lab6)
    - [Create Azure NSGs with Terraform](./Cloud/1-terraform/lab7)
    - [Deploying an Azure VM with Terraform](./Cloud/1-terraform/lab8)
    - [Deploy a Web Application with Terraform](./Cloud/1-terraform/lab9)
    - [Deploy a MySQL Database with Terraform](./Cloud/1-terraform/lab_10)
    - [Migrating Terraform State to Terraform Cloud](./Cloud/1-terraform/lab_11)
    - [Using Terraform Provisioners to Set Up an Apache Web Server on AWS](./Cloud/1-terraform/lab_12)
    - [Make Changes to AWS Infrastructure Using Terraform](./Cloud/1-terraform/lab_13)
    - [Use Output Variables to Query Data in AWS Using Terraform](./Cloud/1-terraform/lab_14)
    - [Make Changes to Azure Infrastructure Using Terraform](./Cloud/1-terraform/lab_15)
    - [Use Output Variables to Query Data in Azure Using Terraform](./Cloud/1-terraform/lab_16)
    - [Use Terraform to Create a Kubernetes Deployment](./Cloud/1-terraform/lab_17)
    - [Manage Kubernetes Resources with Terraform](./Cloud/1-terraform/lab_18)
    - [Use Terraform to Create an EKS Deployment](./Cloud/1-terraform/lab_19)
    - [Troubleshooting a Terraform Deployment](./Cloud/1-terraform/lab_20)
    
  - [Automation Principles](./Cloud/2-automation_principles)
  - [Kubernetes Principles](./Cloud/3-kubernetes_principles)

</details>

## SDLC 

> The Software Development Life Cycle (SDLC) is a structured process used by software developers and project managers to design, develop, test, and deploy software systems.

- SDLC - [What is and how it works](https://agilie.com/blog/what-is-the-software-development-life-cycle-sdlc-and-how-does-it-work)

## SDLC Methodologies

> Below are four common SDLC methodologies, each with its own approach and advantages:

![image](https://github.com/brown9804/SDLC-Cloud_Lpath/assets/24630902/e809d790-87d4-41a1-b9ea-071327ab6ef2)

<details>
  <summary>Waterfall</summary>

  > **Waterfall** is a linear and sequential approach where each phase must be completed before the next begins.
  >
  > - **Phases**: Requirements → Design → Implementation → Testing → Deployment → Maintenance  
  > - **Best for**: Projects with well-defined requirements and low risk of changes  
  > - **Pros**: Simple to manage, clear milestones  
  > - **Cons**: Inflexible to changes, late discovery of issues  
</details>

<details>
  <summary>Agile</summary>

  > **Agile** is an iterative and incremental approach that emphasizes flexibility, collaboration, and customer feedback.
  >
  > - **Phases**: Repeated cycles of planning, development, testing, and review  
  > - **Best for**: Projects requiring frequent updates and stakeholder involvement  
  > - **Pros**: Adaptive to change, faster delivery, continuous improvement  
  > - **Cons**: Requires close collaboration, less predictability  
</details>

<details>
  <summary>Iterative</summary>

  > **Iterative** development builds the system incrementally through repeated cycles (iterations), refining the product with each cycle.
  >
  > - **Phases**: Initial planning → Iteration cycles (Design → Build → Test → Evaluate)  
  > - **Best for**: Projects where requirements evolve over time  
  > - **Pros**: Early delivery of partial systems, easier to manage risk  
  > - **Cons**: Can be resource-intensive, potential for scope creep  
</details>

<details>
  <summary>DevOps</summary>

  > **DevOps** is a culture and set of practices that integrates software development (Dev) and IT operations (Ops) to shorten the development lifecycle.
  >
  > - **Focus**: Automation, continuous integration/continuous delivery (CI/CD), and collaboration  
  > - **Best for**: Projects needing rapid deployment and high reliability  
  > - **Pros**: Faster releases, improved collaboration, better quality  
  > - **Cons**: Requires cultural shift, complex tooling  
</details>

## Secure by

![Benefits](https://github.com/brown9804/SDLC-Cloud_Lpath/assets/24630902/dc014629-a069-44f3-b657-7f8d39968272)

<details>
  <summary>Protocol Testing</summary>

  > **Protocol Testing** ensures that communication protocols are implemented correctly and securely.  
  > - **Purpose**: Validate data exchange rules and detect vulnerabilities in protocol handling  
  > - **Tools**: Wireshark, Postman, SoapUI  
  > - **Benefits**: Prevents miscommunication and exploits in networked systems  
</details>

<details>
  <summary>Automated Testing</summary>

  > **Automated Testing** uses scripts and tools to run tests on code automatically.  
  > - **Purpose**: Quickly detect regressions and security flaws  
  > - **Tools**: Selenium, JUnit, TestNG  
  > - **Benefits**: Increases test coverage and consistency  
</details>

<details>
  <summary>Functional Testing</summary>

  > **Functional Testing** verifies that software behaves according to requirements.  
  > - **Purpose**: Ensure features work as intended, including security-related functions  
  > - **Tools**: QTP, TestComplete, Ranorex  
  > - **Benefits**: Confirms correct behavior under expected conditions  
</details>

<details>
  <summary>Penetration Testing (Pentests)</summary>

  > **Penetration Testing** simulates attacks to find exploitable vulnerabilities.  
  > - **Purpose**: Identify real-world security weaknesses  
  > - **Tools**: Metasploit, Burp Suite, Nessus  
  > - **Benefits**: Helps prioritize and fix critical security issues  
</details>

<details>
  <summary>Dynamic Code Analysis</summary>

  > **Dynamic Code Analysis** evaluates code behavior during execution.  
  > - **Purpose**: Detect runtime vulnerabilities like memory leaks or injection flaws  
  > - **Tools**: Valgrind, Fortify, AppScan  
  > - **Benefits**: Finds issues that static analysis might miss  
</details>

<details>
  <summary>Secure Programming Practices</summary>

  > **Secure Programming Practices** involve writing code with security in mind from the start.  
  > - **Purpose**: Prevent vulnerabilities like buffer overflows, XSS, and SQL injection  
  > - **Examples**: Input validation, least privilege, secure APIs  
  > - **Benefits**: Reduces the number of bugs and security flaws  
</details>

<details>
  <summary>Monitoring and Incident Response</summary>

  > **Monitoring and Incident Response** involves tracking system activity and reacting to threats.  
  > - **Purpose**: Detect and respond to breaches or anomalies in real time  
  > - **Tools**: Splunk, ELK Stack, PagerDuty  
  > - **Benefits**: Minimizes damage and recovery time after incidents  
</details>

## Common Phases

- SDLC - [Methodologies](https://datarob.com/sdlc-methodologies/)

![image](https://github.com/brown9804/SDLC-Cloud_Lpath/assets/24630902/a3b6522f-88c2-4ede-a477-09280f5584b9)

<details>
  <summary>1. Planning Phase</summary>

  > **Planning** involves defining the scope, resources, timeline, and goals of the project.  
  > - **Purpose**: Establish a roadmap and feasibility  
  > - **Key Activities**: Budgeting, scheduling, risk assessment  
  > - **Outcome**: Project plan and initial approval  
</details>

<details>
  <summary>2. Requirement Definition</summary>

  > **Requirement Definition** gathers and documents what the software must do.  
  > - **Purpose**: Understand user needs and system expectations  
  > - **Key Activities**: Stakeholder interviews, use cases, requirement specs  
  > - **Outcome**: Software Requirements Specification (SRS)  
</details>

<details>
  <summary>3. Design and Prototyping</summary>

  > **Design and Prototyping** translates requirements into architecture and UI/UX models.  
  > - **Purpose**: Create a blueprint for development  
  > - **Key Activities**: Wireframes, data models, system architecture  
  > - **Outcome**: Design documents and prototypes  
</details>

<details>
  <summary>4. Rapid Software Development</summary>

  > **Rapid Software Development** focuses on building the software quickly using iterative methods.  
  > - **Purpose**: Deliver working software in short cycles  
  > - **Key Activities**: Coding, version control, agile sprints  
  > - **Outcome**: Functional software modules  
</details>

<details>
  <summary>5. Testing and Quality Assurance</summary>

  > **Testing and QA** ensures the software meets requirements and is free of defects.  
  > - **Purpose**: Validate functionality, performance, and security  
  > - **Key Activities**: Unit tests, integration tests, bug tracking  
  > - **Outcome**: Verified and validated software  
</details>

<details>
  <summary>6. Deployment</summary>

  > **Deployment** involves releasing the software to users or production environments.  
  > - **Purpose**: Make the software available for use  
  > - **Key Activities**: Release planning, environment setup, rollout  
  > - **Outcome**: Live software system  
</details>

<details>
  <summary>7. Operations and Maintenance</summary>

  > **Operations and Maintenance** includes monitoring, support, and updates post-deployment.  
  > - **Purpose**: Ensure long-term stability and performance  
  > - **Key Activities**: Bug fixes, updates, user support  
  > - **Outcome**: Sustained software reliability and improvement  
</details>

![image](https://github.com/brown9804/SDLC-Cloud_Lpath/assets/24630902/5ba714af-4238-48d3-9043-cbcd64a590f1)

<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-1276-limegreen" alt="Total views">
  <p>Refresh Date: 2025-07-22</p>
</div>
<!-- END BADGE -->
