# Use Terraform to Create a Kubernetes Deployment

----------

Costa Rica

Belinda Brown, belindabrownr04@gmail.com

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

April, 2022

----------
This is a summary based on [References](#reference)

### _Connect to the server_:

`ssh <user_name>@<IPadress>`

## Create Your Kubernetes Cluster:
1. Create your Kubernetes cluster: <br/>
`kind create cluster --name lab-terraform-kubernetes --config kind-config.yaml`
2. When the cluster is successfully created, you should see all the creation steps have green checkmarks, and you receive a 'Have a nice day!' message.
3. Copy the provided command and paste it in the terminal: <br/>
`kubectl cluster-info --context kind-lab-terraform-kubernetes`
4. Verify your cluster was created: <br/>
`kind get cluster`


## Configure Terraform for Use with the Kubernetes Cluster:
1. Run kubectl to get information about your cluster: <br/>
`kubectl config view --minify --flatten --context=kind-lab-terraform-kubernetes`
2. Add the server address to your terraform.tfvars file:
- Scroll up to the server line and copy the server address.
- Edit the terraform.tfvars file: <br/>
`vim terraform.tfvars`
- On the host line, enter insert mode and replace DUMMY VALUE with your copied server address.
- Press ESC to exit insert mode, then write and quit to save your changes: `:wq!`
3. Add the client certificate data to your terraform.tfvars file: <br/>
- Scroll up to the client-certificate-data line and copy the full certificate details.
- Edit the terraform.tfvars file: <br/>
`vim terraform.tfvars`
- On the client_certificate line, enter insert mode and replace DUMMY VALUE with your copied client certificate data.
- Press ESC to exit insert mode, then write and quit to save your changes: `:wq!`
4. Add the client key data to your terraform.tfvars file: <br/>
- Scroll up to the client-key-data line and copy the full client key details.
- Edit the terraform.tfvars file: <br/>
`vim terraform.tfvars`
- On the client_key line, enter insert mode and replace DUMMY VALUE with your copied client key data.
- Press ESC to exist insert mode, then write and quit to save your changes: `:wq!`
5. Add the certificate authority data to your terraform.tfvars file: <br/>
- Scroll up to the certificate-authority-data line and copy the full certificate authority details.
- Edit the terraform.tfvars file:<br/> 
`vim terraform.tfvars`
- On the cluster_ca_certificate line, enter insert mode and replace DUMMY VALUE with your copied client authority data.
- Press ESC to exit insert mode, then write and quit to save your changes: `:wq!`
6. View your kubernetes.tf file: <br/>
`vim kubernetes.tf`
> You can see this configuration file pulls from the terraform.tfvars file to declare the variables and then pass them to the Kubernetes provider.
7. Quit out of the file when you're finished reviewing it: `:q`


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

> View your deployment details: <br/>

`kubectl get deployments`

> You should see your deployment, "long-live-the-bat" has two nodes up and running.


## Reminder:

> Later on, remember to do the destroy: <br/>

`$ terraform destroy`

> Enter a value: yes

> Confirm that Terraform is no longer managing any resources: <br/>

`terraform show`

> View a list of the resources Terraform is managing: <br/>

`terraform state list`

## Reference:

[1] From https://learn.acloud.guru/course/bd8060c6-e408-4801-a4a3-8317c45319bf/dashboard <br/>
