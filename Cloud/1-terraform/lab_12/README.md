# Using Terraform Provisioners to Set Up an Apache Web Server on AWS

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


## Examine the Code in the main.tf File:
> View the contents of the main.tf file using the cat command:<br/>

`cat main.tf`

> Examine the code in the resource block and note the following: <br/>
1. We are creating an AWS EC2 instance (virtual machine) named webserver.
2. We are passing a number of parameters for the resource, such as the AMI that the VM will be spun up as, the instance type, the private key that the instance will be using, the public IP attached to the instance, the security group applied to the instance, and the subnet ID where the VM will be spun up.

> Note: All of these resources are actually being created via the setup.tf file, which you can view if desired.

3. Examine the code in the provisioner block and note the following:
- The remote-exec keyword tells us that this is a remote provisioner, which invokes a script on a remote resource after it is created.
- The provisioner is using the parameters configured in the embedded connection block to connect to the AWS EC2 instance being created.
- The provisioner will then issue the commands configured in the inline block to install Apache webserver on CentOS through the yum package manager, start up the Apache server, create a single web page called My Test Website With Help From Terraform Provisioner as an index.html file, and move that file into the data directory of the webserver to be served out globally.



## Deploy the Code and Access the Bootstrapped Webserver:

`export TF_LOG=TRACE`

`export TF_LOG_PATH=./terraform.log`

`$ terraform init`

`$ ls -a`

`$ terraform fmt`

`$ terraform validate`

`$ terraform plan`

`$ terraform apply`

> Enter a value: yes

> As the code is being deployed, you will notice that the Terraform provisioner tries to connect to the EC2 instance, and once that connection is established, it will run the bootstrapping that was configured in the provisioner block against the instance. <br/>

> When complete, it will output the public IP for the Apache webserver as the Webserver-Public-IP value. <br/>

> Copy the IP address, paste it in a new browser window or tab, and press Enter. <br/>

> Verify that the web page displays as My Test Website With Help From Terraform Provisioner, validating that the provisioner within your code worked as intended. The commands configured in the provisioner code were issued and executed successfully on the EC2 instance that was created. <br/>

`$ terraform destroy`

> Enter a value: yes

## Reference:

[1] From https://learn.acloud.guru/course/bd8060c6-e408-4801-a4a3-8317c45319bf/dashboard <br/>

<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-1192-limegreen" alt="Total views">
  <p>Refresh Date: 2025-07-16</p>
</div>
<!-- END BADGE -->
