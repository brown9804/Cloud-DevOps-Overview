# Using Terraform CLI Commands (workspace and state) to Manipulate a Terraform Deployment

----------

Costa Rica

Belinda Brown, belindabrownr04@gmail.com

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Jan, 2022

----------


### _Connect to the server_:

`ssh <user_name>@<IPadress>`


### _Clone files_:

`$ git clone https://github.com/linuxacademy/content-hashicorp-certified-terraform-associate-foundations.git`

`$ ls`

`$ cd content-hashicorp-certified-terraform-associate-foundations/section4-lesson3`

`$ ls`

### _Initialize_:

`$ terraform workspace list`

`$ terraform workspace new test`

`$ terraform init`

`$ cat main.tf`

`$ cat network.tf`

`$ terraform workspace list`

`$ terraform apply --auto-approve` 

`$ terraform state list`

> Inside other workspace

`$ terraform workspace select default`

`$ terraform state list`

`$ cat main.tf`

`$ terraform workspace list`

`$ terraform apply --auto-approve` 

`$ terraform state list`

`$ ls`

> Deleting resources

`$ terraform workspace select test`

`$ terraform destroy --auto-approve` 

`$ terraform workspace select default`

`$ terraform destroy --auto-approve` 

`$ terraform workspace delete test`

`$ terraform workspace list`

## References

[1] From https://help.acloud.guru/hc/en-us/articles/360001382275-Hands-On-Labs-Getting-Started?_ga=2.173162026.84959279.1650153500-266741931.1648820099 <br/>
[2] From https://github.com/linuxacademy/content-hashicorp-certified-terraform-associate-foundations <br/>
[3] From https://releases.hashicorp.com/terraform/0.13.4/ <br/>
[4] From https://learn.acloud.guru/course/using-terraform-to-manage-applications-and-infrastructure/overview
