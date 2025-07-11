# Kubernetes Overview 

Costa Rica

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2025-07-11

----------

## Wiki 

- AKS - [Understanding concepts and docker](https://geekflare.com/docker-vs-kubernetes/)

<img width="758" alt="image" src="https://github.com/brown9804/DevOps-Agile-Cloud_path/assets/24630902/52bc950c-bce2-47cc-8b62-1ca7355ee616">

<img width="733" alt="image" src="https://github.com/brown9804/DevOps-Agile-Cloud_path/assets/24630902/a4312875-2bcc-4b30-a02d-b603829849f8">

- AKS - [Choosing the Right Kubernetes Cluster Approach: Multi-tenancy vs. Multi-cluster](https://www.linkedin.com/pulse/choosing-right-kubernetes-cluster-approach-vs-mina-gobrial?trk=public_post_main-feed-card_reshare_feed-article-content), Difference Between multi-cluster, multi-master, multi-tenant & federated Kubernetes [click here](https://platform9.com/blog/difference-between-multi-cluster-multi-master-multi-tenant-federated-kubernetes/)

<img width="958" alt="image" src="https://github.com/brown9804/DevOps-Agile-Cloud_path/assets/24630902/7cc8c40f-3c47-4b98-85b4-378a35dac9af">

| Single/Multi Tenants | Federated | 
| --- | --- |
| <img alt="image" src="https://github.com/brown9804/DevOps-Agile-Cloud_path/assets/24630902/62c06ee7-d682-4870-8727-edda6eabe18c"> | <img alt="image" src="https://github.com/brown9804/DevOps-Agile-Cloud_path/assets/24630902/14367694-c2df-4eaf-ae41-68ee088d3fec"> |  

- AKS - [Understanding Multi-Cluster Kubernetes: Architecture, Benefits, and Challenges](https://traefik.io/glossary/understanding-multi-cluster-kubernetes/), Why would I want to use a multi-cluster architecture?, to understand that and difference between segmentation, and replication [click here](https://www.redhat.com/architect/multi-cluster-kubernetes-architecture)

| Component | Definition | URL | 
| ---- | --- | --- |
| Kubernetes | Is an open source system to deploy, scale, and manage containerized applications anywhere. | [What is k8s](https://cloud.google.com/learn/what-is-kubernetes) |
| Container | A container is a standalone object that holds everything an application needs to execute, including libraries, resource files, and configuration files. Containers are lightweight compared to virtual machines and can run regardless of infrastructure or environment. This makes them ideal for ease-of-management across devices and operating systems. | [What is k8s container?](https://avinetworks.com/glossary/kubernetes-container/#:~:text=A%20Kubernetes%20container%20cluster%20serves,pod%20and%20houses%20the%20cluster.) |
| Pod | A container or group of containers running on a machine.  | [What is k8s pods?](https://www.vmware.com/topics/glossary/content/kubernetes-pods.html)|
| Node | A node is a physical or virtual machine that operates at least a single container, though they can (and often) run multiple containers. | [What is ks8 node?](https://www.cloudzero.com/blog/kubernetes-nodes/) |
| Cluster |  A cluster is a set of virtual or physical machines, each operating as a nod to run containerized applications. Clusters are managed by Kubernetes. |[What is k8s cluster?](https://www.oracle.com/cloud/cloud-native/container-engine-kubernetes/what-is-kubernetes/cluster/) |
| Deployment | Deployment refers to the process of installing, executing, or updating containers on a node. Efficient deployment takes advantage of tools such as automation to simplify management and resource usage. | [Reference here](https://www.vmware.com/topics/glossary/content/kubernetes-deployment.html#:~:text=A%20Kubernetes%20Deployment%20tells%20Kubernetes,earlier%20deployment%20version%20if%20necessary.) |
| Replicaset | A tool used to ensure availability, Replicaset defines the quantity of stable replica Pods that must be running at any one time, then manages resources to fulfill this. Replicaset creates or deletes Pods to meet and maintain the target. | [Reference here](https://sysdig.com/learn-cloud-native/kubernetes-101/kubernetes-replicasets-overview/#:~:text=A%20ReplicaSet%20(RS)%20is%20a,nevertheless%2C%20short%2Dlived%20entities.) | 
| Orchestration | Container orchestration operates one level above deployment and refers to the overall management and operational logistics that oversee containers. Orchestration is necessary to balance resources in an extremely dynamic environment. | [Reference here](https://www.vmware.com/topics/glossary/content/container-orchestration.html#:~:text=What%20is%20Kubernetes%20container%20orchestration,schedule%20and%20monitor%20those%20containers.) | 

<img width="1067" alt="image" src="https://github.com/brown9804/DevOps-Agile-Cloud_path/assets/24630902/6b16a8d4-f3f9-4843-bce7-e421630e04f3">

<img width="1098" alt="image" src="https://github.com/brown9804/DevOps-Agile-Cloud_path/assets/24630902/2a73bda1-4ea9-4d04-b3e7-99e9e8baee48">

- AKS - [Quickstart: Deploy an Azure Kubernetes Service (AKS) cluster using Azure portal](https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-portal?tabs=azure-cli)
- AKS - [Quickstart: Deploy an Azure Kubernetes Service (AKS) cluster using Terraform](https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-terraform?tabs=bash), and other refence [deploying a fully configured AKS cluster in Azure using Terraform](https://blog.bart.je/deploying-a-fully-configured-aks-cluster-in-azure-using-terraform/)

<img width="950" alt="image" src="https://github.com/brown9804/SDLC-Cloud_Lpath/assets/24630902/634cb234-81f9-4336-8919-bb5bfca3a4ea">

<img width="950" alt="image" src="https://github.com/brown9804/SDLC-Cloud_Lpath/assets/24630902/fc48afeb-4f0c-4a27-9055-1dcd4a90405a">

<img width="950" alt="image" src="https://github.com/brown9804/SDLC-Cloud_Lpath/assets/24630902/d17da6a3-9c0c-4e50-807f-de3cbebbc5e0">


<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-456-limegreen" alt="Total views">
  <p>Refresh Date: 2025-07-11</p>
</div>
<!-- END BADGE -->
