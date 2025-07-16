# Migrating Terraform State to Terraform Cloud

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


### _Generate Your Access Key in the AWS Management Console_:
1. In a browser window, navigate to the AWS Management Console and log in with the credentials provided.
2. Under AWS services, click IAM.
3. On the IAM dashboard, under IAM resources, click Users.
4. In the list of users, click cloud_user.
5. Click the Security credentials tab.
6. Click the Create access key button.
7. In the Create access key pop-up, click the Download .csv file button to download the access key in a file.
> Note: You could also choose to copy and paste the Access key ID and Secret access key values directly from the Create access key pop-up in the next objective.


## Set Up Your Terraform Cloud Workspace:
### _Create the Workspace and Configure Your Environment Variables_:
1. In a new browser tab, navigate to https://app.terraform.io/session.
2. Click Create account and follow the prompts to create a new free account or click Sign in to log in with an existing account.
3. Once logged in, select the Start from scratch setup workflow option.
4. In the Organization name field, enter "ACG-Terraform-Labs".
> NOTE: If this name is already taken you can make your own name up for your organisation.
5. In the Email address field, enter your email address.
6. Click Create organization.
7. Select the CLI-driven workflow option.
8. In the Workspace Name field, enter "lab-migrate-state".
9. Click Create workspace.
10. In the workspace, click on the Variables tab.
11. Scroll down to the Environment Variables section, and click the + Add variable button.
12. In the Key field, type "AWS_ACCESS_KEY_ID".
13. In the Value field, copy and paste the Access key ID value from the Create access key pop-up in the AWS Management Console or from the CSV file you downloaded.
14. Select the Sensitive checkbox, and click Save variable.
15. Click the + Add variable button.
16. In the Key field, type "AWS_SECRET_ACCESS_KEY".
17. In the Value field, copy and paste the Secret access key value from the Create access key pop-up in the AWS Management Console or from the CSV file you downloaded.
18. Select the Sensitive checkbox, and click Save variable.


### _Create Your API Token for Terraform CLI Login_:
1. At the top-right of the Terraform Cloud window, click your user avatar and select User settings.
2. In the menu on the left, click Tokens.
3. Click Create an API token.
4. In the Description field, type "terraform_login".
5. Click Create API token.
6. Copy the API token that is displayed in the Create API token pop-up and click Done.
> Note: Be sure that you have copied the API token, as it will not be displayed again. You may want to paste it in an accessible location, just in case.
7. At the top-left of the Terraform Cloud window, click the Choose an organization drop-down and select ACG-Terraform-Labs.
8. In the list of workspaces, click lab-migrate-state.


## Adding the Backend Configuration:

1. Back in the terminal, log in to Terraform Cloud from the CLI: <br/>
`terraform login`
2. Uncomment the backend config within the main.tf
3. Save it.
4. Check that the configuration file has been formatted properly: <br/>
`terraform fmt`
5. Initialize the working directory: <br/>
`terraform init`
6. When prompted to copy the existing Terraform state to the new backend, type "yes" and hit Enter. Terraform will notify you when this has completed successfully.
7. Verify that the terraform.tfstate.backup file has been added to the directory: <br/>
`ls
8. Delete the terraform.tfstate file: <br/>
`rm -rf terraform.tfstate`


## Apply the Updated Configuration and Confirm the State Was Saved to Terraform Cloud:
1. Apply the updated configuration: <br/>
`terraform apply`
2. Once the terraform apply has finished, navigate back to Terraform Cloud in the browser.
3. On the Overview tab for the workspace, verify that the last run appears as a new event in the Latest Run section and that 1 resource was applied under Resources.
4. Click on the States tab and verify that the state file appears. You can click on the file to view it.
5. Click on the Runs tab and view the latest runs that have completed.
6. To view more information about the run, click on the Overview tab and click the See details button for the run.

## Reminder:

>> Later on, remember to do the destroy:

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
