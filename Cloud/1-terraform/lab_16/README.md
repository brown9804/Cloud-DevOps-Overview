# Use Output Variables to Query Data in Azure Using Terraform


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

## Deploy the Infrastructure:

1. Under # Create a virtual network, next to resource_group_name, remove the filler name.
2. At the top of the screen, above the Cloud Shell terminal, copy the name of the resource group automatically created by this lab, above Resource group.
3. Paste it into the empty field next to resource_group_name.
4. Under #Create subnet, next to resource_group_name, delete the filler and paste our lab's resource group name.
5. Save and quit by pressing the Escape button and entering: `:wq`


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


## Add the Outputs Variable File:

> output.tf file added

`$ terraform fmt`

`$ terraform plan`

`$ terraform apply`

> Enter a value: yes

> Display our outputs: <br/>

`terraform output`

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

<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-1276-limegreen" alt="Total views">
  <p>Refresh Date: 2025-07-22</p>
</div>
<!-- END BADGE -->
