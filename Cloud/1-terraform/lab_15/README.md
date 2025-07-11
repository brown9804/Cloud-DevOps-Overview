# Make Changes to Azure Infrastructure Using Terraform

Costa Rica

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2025-07-10

----------

This is a summary based on [References](#reference)

## _Connect to the server_:

`ssh <user_name>@<IPadress>`


## _Update the virtual network's resource_group_name_:
1. Above Cloud Shell, copy your Azure resource group name. You may need to pull down your Cloud Shell terminal to see it.
2. To the right of the resource_group_name variable, replace <ADD YOUR RESOURCE GROUP> with your copied resource group name.
3. Write and quit to save your changes: `:wq!`


### _Initializes_:

`export TF_LOG=TRACE`

`export TF_LOG_PATH=./terraform.log`

`$ terraform init`

`$ ls -a`

`$ terraform fmt`

`$ terraform validate`

`$ terraform plan`

`$ terraform apply`

> Enter a value: yes

> To confirm that our configuration was successful and view all the details of our infrastructure: <br/>

`terraform show`

> View a list of the resources Terraform is managing: <br/>

`terraform state list`

## Add a Subnet to the Configuration:
1. Edit the file: <br/>
`vim azure_resource_block.tf`
2. Update the subnet's resource_group_name:
-  Above Cloud Shell, copy your Azure resource group name.
- To the right of the resource_group_name variable, replace <ADD YOUR RESOURCE GROUP> with your copied resource group name.
- Write and quit to save your changes: `:wq!`

`$ terraform plan`

`$ terraform apply`

> Enter a value: yes

> To confirm that our configuration was successful and view all the details of our infrastructure: <br/>

`terraform show`

> View a list of the resources Terraform is managing: <br/>

`terraform state list`


## Add a Tag to the Configuration:

1. Uncomment the tag part within the main.tf.
2. Save it.

`$ terraform fmt`

`$ terraform validate`

`$ terraform plan`

`$ terraform apply`

> Enter a value: yes

> To confirm that our configuration was successful and view all the details of our infrastructure: <br/>

`terraform show`

> View a list of the resources Terraform is managing: <br/>

`terraform state list`


## Reminder:

>> Later on, remember to do the destroy:

`$ terraform destroy`

> Enter a value: yes

>> Confirm that Terraform is no longer managing any resources: <br/>
`terraform show`

> View a list of the resources Terraform is managing: <br/>

`terraform state list`


## Reference:

[1] From https://learn.acloud.guru/course/bd8060c6-e408-4801-a4a3-8317c45319bf/dashboard <br/>

<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-195-limegreen" alt="Total views">
  <p>Refresh Date: 2025-07-10</p>
</div>
<!-- END BADGE -->
