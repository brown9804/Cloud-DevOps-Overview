# Installing Terraform and Working with Terraform Providers

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

### _Download zip_:

`$ wget -c <location>`

For Windows:<br/>

> See [Install Terraform On Windows 10 – Learn IT And DevOps Daily](https://github.com/brown9804/DevOps-Agile-Cloud_path/blob/main/Cloud/_docs/refs/Install%20Terraform%20On%20Windows%2010%20%E2%80%93%20Learn%20IT%20And%20DevOps%20Daily.pdf)


Binary List link:https://releases.hashicorp.com/terraform

Recommended: https://releases.hashicorp.com/terraform/0.13.4/

### _Unzip_:

`$ unzip terraform_0.13.4_linux_amd64.zip`

`$ ls`

### _Move dir to be accessed_:

`$ sudo mv terraform /usr/sbin`

`$ ls`

`$ terraform version`

### _Access providers_:

`$ mkdir providers`

`$ cd providers/`

`$ ls`

`$ vim main.tf`

`$ cat main.tf`

`$ export TF_LOG=TRACE`

`export TF_LOG_PATH=./terraform.log`  


### _Initializes_:

`$ terraform init`

`$ ls -a`

`$ terraform fmt`

`$ terraform plan`

`$ terraform apply`

> Enter a value: yes

`$ terraform destroy`

> Enter a value: yes

## References 

[1] From https://help.acloud.guru/hc/en-us/articles/360001382275-Hands-On-Labs-Getting-Started?_ga=2.173162026.84959279.1650153500-266741931.1648820099 <br/>
[2] From https://github.com/linuxacademy/content-hashicorp-certified-terraform-associate-foundations <br/>
[3] From https://releases.hashicorp.com/terraform/0.13.4/ <br/>
[4] From https://learn.acloud.guru/course/using-terraform-to-manage-applications-and-infrastructure/overview

<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-1276-limegreen" alt="Total views">
  <p>Refresh Date: 2025-07-22</p>
</div>
<!-- END BADGE -->