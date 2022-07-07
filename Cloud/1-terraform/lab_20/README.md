# Troubleshooting a Terraform Deployment

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

## Correct the Variable Interpolation Error:
1. Edit the ami in the main.tf file.
- In the resource block, edit the ami line by replacing <DUMMY VALUE> with your copied AMI.
2. Edit the subnet_id in the main.tf file:
- In the resource block, edit the subnetid line by replacing <DUMMY VALUE> with your copied subnet ID.

`export TF_LOG=TRACE`

`export TF_LOG_PATH=./terraform.log`

`$ ls -a`

`$ terraform fmt`

3. Apply line numbering to the file so you can identify the error more easily: <br/>
`:set number`
4. Update line 25 as follows to correct the variable interpolation error: <br/>
`Name = "${var.name}-learn"`

`$ terraform fmt`

`$ terraform init`


## Correct the Region Declaration Error:

`$ terraform validate`

1. Check the variables.tf file: <br/>
`vim variables.tf`
> You should see the variable regions, which is causing the error. This should instead be region.

2. Update regions to region in the variables.tf file to correct the region declaration error: <br/>
```
variable "region" {
  description = 'The AWS region your resources will be deployed'
}
```

## Correct the Syntax Error for the Resource:

`$ terraform validate`

1. Edit the main.tf file. 
2. Insert double quotes ("") around the ami and subnet_id values as follows to correct the syntax error: <br/>
```
resource "aws_instance" "web_app"
  ami         = "ami-<YOUR_AMI_ID>"
  subnet_id   = "subnet-<YOUR_SUBNET_ID>"
```

## Correct the Outputs Error:

`$ terraform validate`

1. Edit the outputs.tf file.
2. Correct the first output error by changing the instance_public_ip value from .public.ip to .pulic_ip as follows: <br/>
```
output "instance_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.web_app.public_ip
}
```
3. Correct the second output error by changing the instance_name value from tag to tags as follows: <br/>
```
output "instance_name" {
  description = "Tags of the EC2 instance"
  value       = aws_instance.web_app.tags.Name
}
```

## Deploy the Infrastructure:

`$ terraform validate`

`$ terraform plan`

`$ terraform apply`

> Enter a value: yes

## Reminder:

> Later on, remember to do the destroy: <br/>

`$ terraform destroy`

> Enter a value: yes

`terraform show`

## Reference:

[1] From https://learn.acloud.guru/course/bd8060c6-e408-4801-a4a3-8317c45319bf/dashboard <br/>
