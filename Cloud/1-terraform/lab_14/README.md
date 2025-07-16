# Use Output Variables to Query Data in AWS Using Terraform

Costa Rica

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

April, 2022

----------

This is a summary based on [References](#reference)

## _Connect to the server_:

`ssh <user_name>@<IPadress>`

## Set Up the Environment:

### _Set Up and Apply Your Terraform Configuration_:

1. In the ami = line, delete the "DUMMY_VALUE_AMI_ID" value and paste in the AMI you copied from the resource_ids.txt file.
2. Save and exit the file by pressing the Escape key and entering :wq!.
3. Open the resource_ids.txt file again: <br/>
`vim ../resource_ids.txt`
4. Copy the subnet _id value.
5. Exit the file by pressing Escape and entering :q!.
6. Open the main.tf file for editing: <br/>
`vim main.tf`
7. In the subnet_id = line, delete the "DUMMY_VALUE_SUBNET_ID" and paste in the subnet ID you copied from the resource_ids.txt file.
8. Save and exit the file by pressing the Escape key and entering :wq!.

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


> Add Output Variables and Deploy Changes: <br/>

`$ terraform fmt`

### _Confirm the Changes_:

`$ terraform plan`

`$ terraform apply`

> Enter a value: yes

> View a simplified version of the output: <br/>

`terraform output`

> To confirm that our configuration was successful and view all the details of our infrastructure: <br/>

`terraform show`


## Reminder:

> Later on, remember to do the destroy: <br/>

`$ terraform destroy`

> Enter a value: yes

> Confirm that Terraform is no longer managing any resources: <br/>

`terraform show`

## Reference:

[1] From https://learn.acloud.guru/course/bd8060c6-e408-4801-a4a3-8317c45319bf/dashboard <br/>

<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-1192-limegreen" alt="Total views">
  <p>Refresh Date: 2025-07-16</p>
</div>
<!-- END BADGE -->

Last updated: 2025-07-11
