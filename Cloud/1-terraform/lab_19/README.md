# Use Terraform to Create an EKS Deployment

Costa Rica

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2025-07-11

----------

This is a summary based on [References](#reference)

## _Connect to the server_:

`ssh <user_name>@<IPadress>`

## Configure the AWS CLI:
`aws configure`

1. When prompted for your AWS Access Key ID, copy and paste the Access Key.
2. When prompted for your AWS Secret Access Key, copy and paste in the Secret Access Key.
3. Press Enter to accept the default region.
4. Press Enter to accept the default output.

## Deploy the EKS Cluster:

`export TF_LOG=TRACE`

`export TF_LOG_PATH=./terraform.log`

`$ terraform init`

`$ ls -a`

`$ terraform fmt`

`$ terraform validate`

`$ terraform plan`

`$ terraform apply`

> Enter a value: yes

> Configure kubectl to interact with the cluster: <br/>

`aws eks --region $(terraform output -raw region) update-kubeconfig --name $(terraform output -raw cluster_name)`

> Confirm that kubectl was configured properly and that the cluster was successfully deployed: <br/>

`kubectl get cs`

> The three components should be up and running with a status of Healthy.

## Deploy the NGINX Pods:

`$ terraform plan`

`$ terraform apply`

> Enter a value: yes

`kubectl get deployments`

## Reminder:

> Later on, remember to do the destroy: <br/>

`$ terraform destroy`

> Enter a value: yes

`terraform show`

## Reference:

[1] From https://learn.acloud.guru/course/bd8060c6-e408-4801-a4a3-8317c45319bf/dashboard <br/>

<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-195-limegreen" alt="Total views">
  <p>Refresh Date: 2025-07-10</p>
</div>
<!-- END BADGE -->
