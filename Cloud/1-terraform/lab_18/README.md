# Manage Kubernetes Resources with Terraform

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

## Set Up the Lab Environment:
1. Create your Kubernetes cluster: <br/>
`kind create cluster --name lab-terraform-kubernetes --config kind-config.yaml`
2. When the cluster is successfully created, you should see all the creation steps have green checkmarks, and you receive a 'Have a nice day!' message.
3. Copy the provided command and paste it in the terminal: <br/>
`kubectl cluster-info --context kind-lab-terraform-kubernetes`
4. Verify your cluster was created: <br/>
`kind get cluster`
5. Edit the cluster's host address: <br/>
- Run kubectl to view the cluster's host address: <br/>
`kubectl config view --minify --flatten --context=kind-lab-terraform-kubernetes`
- Copy the server address.
- Edit the variables file: <br/>
`vim terraform.tfvars`
- On the host line, replace [DUMMY VALUE] with your copied server address.
- Write and quit to save the file: <br/>
`:wq!`
6. Edit the cluster's SSL certificate:
- Copy the full client-certificate-data details.
- Edit the variables file: <br/>
`vim terraform.tfvars`
- On the client_certificate line, replace [DUMMY VALUE] with your copied client-certificate-data details.
- Write and quit to save the file: `:wq!`
7. Edit the cluster's client key data:
- Copy the full client-key-data details.
- Edit the variables file: <br/>
`vim terraform.tfvars`
- On the client_key line, replace [DUMMY VALUE] with your copied client-key-data details.
- Write and quit to save the file:`:wq!`
8. Edit the cluster's certificate authority data: <br/>
- Copy the full certificate-authority-data details.
- Edit the variables file: <br/>
`vim terraform.tfvars`
- On the cluster_ca_certificate line, replace [DUMMY VALUE] with your copied certificate-authority-data details.
- Write and quit to save the file:`:wq!`


## Deploy Resources to the Kubernetes Cluster:

`export TF_LOG=TRACE`

`export TF_LOG_PATH=./terraform.log`

`$ terraform init`

`$ ls -a`

`$ terraform fmt`

`$ terraform validate`

`$ terraform plan`

`$ terraform apply`

> Enter a value: yes


## Add a Service:

`$ terraform apply`

> Enter a value: yes

1. Verify the NodePort service was applied successfully: <br/>
`kubectl get services`
> You should see the NodePort service named robin listed in your services.

## Scale the Nodes:
1. Edit the lab_kubernetes_resources.tf file: <br/>
`vim lab_kubernetes_resources.tf`
2. Modify the replicas from 2 to 4:
```
spec {
replicas = 4
selector {
  match_labels = {
    App = "longlivethebat"
  }
}
```
3. Write and quit to save your change to the file: `:wq!` 

`$ terraform apply`

> Enter a value: yes

> Confirm the replicas were changed from 2 to 4, then type "yes" on the Enter a value line to confirm the apply.
4. Verify your deployment is now using 4 pods:
`kubectl get deployments`

## Reminder:

> Later on, remember to do the destroy: <br/>

`$ terraform destroy`

> Enter a value: yes

> Delete your cluster: <br/>

`kind delete cluster --name lab-terraform-kubernetes`

> Verify the cluster was deleted: <br/>

`kind get clusters`

## Reference:

[1] From https://learn.acloud.guru/course/bd8060c6-e408-4801-a4a3-8317c45319bf/dashboard <br/>

<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-673-limegreen" alt="Total views">
  <p>Refresh Date: 2025-07-14</p>
</div>
<!-- END BADGE -->
