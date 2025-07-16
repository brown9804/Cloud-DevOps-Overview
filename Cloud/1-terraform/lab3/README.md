# Exploring Terraform State Functionality

Costa Rica

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2025-07-11

----------

This is a summary based on [References](#references)

## _Connect to the server_:

`ssh <user_name>@<IPadress>`

## _Initialize_:

`$ terraform version`

`$ minikube status`

`$ ls`

`$ cd lab_code/`

`$ ls`

`$ cd section2-hol1/`

`$ ls`

`$ cat main.tf`

`$ terraform init`

`$ terraform plan`

`$ ls`

`$ terraform apply --auto-approve`

`$ ls`

`$ kubectl get pods`

`$ terraform state list`

`$ terraform state show kubernetes_deployment.tf-k8s-deployment | egrep replicas`

`$ vim main.tf` 

_Change replicas from 2 to 4_

`$ terraform plan`	

`$ terraform apply --auto-approve`

`$ kubectl get pods`

`$ terraform state show kubernetes_deployment.tf-k8s-deployment | egrep replicas`

`$ terraform destroy --auto-approve`

`$ kubectl get pods`

`$ ls`

`$ cat terraform.tfstate`

`$ less terraform.tfstate.backup`

_You can re-deploy using backup file_


## References

[1] From https://help.acloud.guru/hc/en-us/articles/360001382275-Hands-On-Labs-Getting-Started?_ga=2.173162026.84959279.1650153500-266741931.1648820099 <br/>
[2] From https://github.com/linuxacademy/content-hashicorp-certified-terraform-associate-foundations <br/>
[3] From https://releases.hashicorp.com/terraform/0.13.4/ <br/>
[4] From https://learn.acloud.guru/course/using-terraform-to-manage-applications-and-infrastructure/overview

<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-1192-limegreen" alt="Total views">
  <p>Refresh Date: 2025-07-16</p>
</div>
<!-- END BADGE -->
