# Make Changes to AWS Infrastructure Using Terraform

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

## Deploy Configuration Changes:
1. Open the main.tf file in the current directory for editing: <br/>
`vim main.tf`
2. Under the resource line, in the instance_type line, delete "t2.micro".
3. In the empty instance_type = line, enter "t3.micro".
4. Under the tags line, in the Name = line, delete "Batman".
5. In the empty Name = line, enter in "Robin".
6. Save and exit the file by pressing the Escape key and entering: `:wq`
7. Check that our format is correct: <br/>
`terraform fmt`
8. Test the changes that we're going to make: <br/>
`terraform plan`
9. Apply our configuration changes: <br/>
`terraform apply`
> Enter a value: yes

10. Confirm that our changes were made successfully: <br/>
`terraform show`
> Check that instance_type is now set to t3.micro and the tags_all has the name set to Robin.


## Reminder:

> Later on, remember to do the destroy:

`$ terraform destroy`

> Enter a value: yes

> Confirm that Terraform is no longer managing any resources: <br/>

`terraform show`

## Reference:

[1] From https://learn.acloud.guru/course/bd8060c6-e408-4801-a4a3-8317c45319bf/dashboard <br/>

<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-195-limegreen" alt="Total views">
  <p>Refresh Date: 2025-07-10</p>
</div>
<!-- END BADGE -->
