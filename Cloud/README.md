# Cloud Principles Overview

----------------------
Costa Rica

Belinda Brown, belindabrownr04@gmail.com

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/) [brown9804](https://github.com/brown9804)


March, 2022

----------------------

## Content:

<details>
<summary><b>Table of Contents</b> (click to open)</summary>
<!-- MarkdownTOC -->
  
- [0. API Currency Exchange Example](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/0-api_curr_exchange_eg)
- [1. Terraform](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform)
  - [Installing Terraform and Working with Terraform Providers](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab0)
  - [Using Terraform CLI Commands (workspace and state) to Manipulate a Terraform Deployment](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab1)
  - [Building and Testing a Basic Terraform Module](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab2)
  - [Exploring Terraform State Functionality](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab3)
  - [Deploy an Azure Storage Account with Terraform](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab4)
  - [Deploy an Azure File Share and Blob Storage with Terraform](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab5)
  - [Deploy Azure VNETs and Subnets with Terraform](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab6)
  - [Create Azure NSGs with Terraform](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab7)
  - [Deploying an Azure VM with Terraform](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab8)
  - [Deploy a Web Application with Terraform](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab9)
  - [Deploy a MySQL Database with Terraform](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab_10)
  - [Migrating Terraform State to Terraform Cloud](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab_11)
  - [Using Terraform Provisioners to Set Up an Apache Web Server on AWS](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab_12)
  - [Make Changes to AWS Infrastructure Using Terraform](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab_13)
  - [Use Output Variables to Query Data in AWS Using Terraform](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab_14)
  - [Make Changes to Azure Infrastructure Using Terraform](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab_15)
  - [Use Output Variables to Query Data in Azure Using Terraform](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab_16)
  - [Use Terraform to Create a Kubernetes Deployment](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab_17)
  - [Manage Kubernetes Resources with Terraform](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab_18)
  - [Use Terraform to Create an EKS Deployment](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab_19)
  - [Troubleshooting a Terraform Deployment](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/1-terraform/lab_20)
- [2. Linux](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/2-linux)
  - [Working with Users and Permissions](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/2-linux/lab0)
  - [System Service Management, Runlevels and Boot Targets](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/2-linux/lab1)
  - [Securely Accessing Your System](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/2-linux/lab2)
  - [Package Management and Troubleshooting](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/2-linux/lab3)
  - [File Management, Permissions and Backup](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/2-linux/lab4)
  - [Working with Text Files and Streams](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/2-linux/lab5)
  - [Linux Device Management](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/2-linux/lab6)
  - [The Linux Shell](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/2-linux/lab7)
  - [Networking](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/2-linux/lab8)
  - [Processes Management](https://github.com/brown9804/DevOps-Agile-Cloud_path/tree/main/Cloud/2-linux/lab9)

<!-- /MarkdownTOC -->
</details>


- Cloud computing - [What is?](https://www.spiceworks.com/tech/cloud/articles/what-is-cloud-computing/). [A Brief History of Cloud Computing](https://www.dataversity.net/brief-history-cloud-computing/). About what is [Project MAC](https://www.darpa.mil/about-us/timeline/project-mac)
<img width="801" alt="image" src="https://github.com/brown9804/DevOps-Agile-Cloud_path/assets/24630902/1b80fe83-6377-4c73-aea1-12b1575cacc8">

<img width="692" alt="image" src="https://github.com/brown9804/DevOps-Agile-Cloud_path/assets/24630902/bf849a7b-9cc7-494c-88e3-fedc39738a35">

- Cloud computing - Service Models: SAAS, PAAS, IAAS - Which Is Better For Business](https://dev.to/artemkobilinskiy/cloud-service-models-saas-paas-iaas-which-is-better-for-business-574k), more details [here](https://qualitapps.com/en/what-are-the-iaas-paas-and-saas-cloud-service-models/)
<img width="709" alt="image" src="https://github.com/brown9804/DevOps-Agile-Cloud_path/assets/24630902/7bc73a87-3b57-4f41-87de-5e72f3dfc6c7">

<img width="642" alt="image" src="https://github.com/brown9804/DevOps-Agile-Cloud_path/assets/24630902/9d9cb10d-c74f-49e9-9cbf-73e7fba68746">

- Cloud computing - Single tenant vs. Multi-tenant services](https://karliris62.medium.com/single-tenant-vs-multi-tenant-cloud-architecture-which-one-to-choose-and-why-8e962eaf8d7c) and [How to Choose for Your Organization](https://resources.igloosoftware.com/blog/multi-tenancy-database/)
<img width="667" alt="image" src="https://github.com/brown9804/DevOps-Agile-Cloud_path/assets/24630902/b3e11d52-47ef-4ff0-b230-031a912084a9">


## Wiki:
- pip - [How to install in macOS](https://phoenixnap.com/kb/install-putty-on-mac)
- pip - [sudo: npm: command not found](https://stackoverflow.com/questions/31472755/sudo-npm-command-not-found)
- Terraform Environment Variables - [export log files](https://www.terraform.io/cli/config/environment-variables)
- Terraform - [How to enable debug logging](https://www.suse.com/support/kb/doc/?id=000020022)
- Terraform - [Custom Condition Checks](https://www.terraform.io/language/expressions/custom-conditions#input-variable-validation)
- Terraform - [Add Disk Bursting for VM Scale Sets](https://github.com/hashicorp/terraform-provider-azurerm/issues/15392)
- Terraform - [Azure managed disks general information](https://learn.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview), see disk types, and disk redundancy options as well. The structure related to the [azurerm_managed_disk](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/managed_disk), and you can find more references of which VM are able to enable this property [here](https://github.com/hashicorp/terraform-provider-azurerm/pull/14137)
- CMD - ['export' is not recognized as an internal or external command](https://stackoverflow.com/questions/26368306/export-is-not-recognized-as-an-internal-or-external-command)
- GitHub - [How to solve the Filename too long error when using `git clone` in windows](https://www.bswen.com/2021/12/how-to-solve-filename-too-long-error-when-using-git-clone-in-windows.html). Solution 2.2.2 might be useful, if not go to [How to Make Windows 10 Accept File Paths Over 260 Characters](https://www.howtogeek.com/266621/how-to-make-windows-10-accept-file-paths-over-260-characters/). And, if that does not fix this try using Git Bash, WSL, or the Command Prompt.
- GitHub - [Useful Git Configuration Items, like better compression](https://wildlyinaccurate.com/useful-git-configuration-items/)
- GitHub - [REST API Search](https://docs.github.com/en/rest/search#text-match-metadata)
- GitHub - [Clone a single branch](https://stackoverflow.com/questions/1778088/how-do-i-clone-a-single-branch-in-git)
- GitHub - [Connecting to GitHub with SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
- Azure Bastion - [What is?](https://docs.microsoft.com/en-us/azure/bastion/bastion-overview), to modify a SSH file on mac click [here](https://stackoverflow.com/questions/54133300/how-to-access-and-modify-a-ssh-file-on-mac)
- PuTTY (a free SSH and Telnet client) - [Donwload on Windows](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html), and on for macOS go [here](https://www.makeuseof.com/putty-for-mac/), or use the bastion which is easier, here you can find [3 Connecting to Windows VMs using Azure Bastion](https://harvestingclouds.com/post/simplifying-azure-bastion-3-connecting-to-windows-vms-using-azure-bastion/#:~:text=Connecting%20to%20the%20Windows%20VM,button%20on%20the%20next%20screen.)
- SSH - [Setting Up Keys](https://cs4118.github.io/dev-guides/vm-ssh.html#setting-up-ssh-keys), [connect to Azure Virtual Desktop with the Remote Desktop client for macOS](https://learn.microsoft.com/en-us/azure/virtual-desktop/users/connect-macos)
- VM - [3 Simple Ways to Transfer Files from a VM to a Host](https://www.nakivo.com/blog/3-simple-ways-to-transfer-files-from-a-vm-to-a-host/) or maybe use this one [How To Transfer Files Between Servers Using SSH](https://www.plesk.com/blog/various/how-to-transfer-files-between-servers-using-ssh/). Which basically needs ssh in local server, and within the other VM: `scp file_to_moved.zip user@ip_server:~/`
- Docker - [How do I start the docker daemon on macOS?](https://apple.stackexchange.com/questions/373888/how-do-i-start-the-docker-daemon-on-macos)
- SSMS (SQL Server Management Studio) – [how to save results with headers](https://solutioncenter.apexsql.com/sql-server-management-studio-ssms-how-to-save-results-with-headers/)
- SSMS - [How to install on Windows](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16#download-ssms), but if you need a tool that runs on operating systems other than Windows, we recommend [Azure Data Studio](https://learn.microsoft.com/en-us/sql/azure-data-studio/download-azure-data-studio?view=sql-server-ver16). Azure Data Studio is a cross-platform tool that runs on macOS, Linux, as well as Windows.
- SSMS - [Database Diagram](https://www.mssqltips.com/sqlservertip/6269/sql-server-database-diagram-tool-in-management-studio/)
- SSMS - [Script objects](https://docs.microsoft.com/en-us/sql/ssms/tutorials/scripting-ssms?view=sql-server-ver16)
- SSMS - [How to Export Tables from a Database](https://documentation.alphasoftware.com/pages/HowTo/Databases/Export%20Tables%20from%20a%20Database.xml)
- SQL - [Replacing one value with another](https://stackoverflow.com/questions/14212814/sql-replacing-one-value-with-another)
- SQL - [Difference between COMMIT and ROLLBACK](https://www.geeksforgeeks.org/difference-between-commit-and-rollback-in-sql/)
- SQL - [GROUP BY Statement](https://www.w3schools.com/sql/sql_groupby.asp)
- SQL - [join tables with group by and order by](https://www.w3resource.com/sql/joins/joining-with-group-by-and-order-by.php)
- SQL - [How to Find Records with NULL in a Column](https://learnsql.com/cookbook/how-to-find-records-with-null-in-a-column/)
- SQL - [Commenting and Uncommenting Code](https://zarez.net/?p=1581#:~:text=SQL%20Server%20Startup-,Commenting%20and%20Uncommenting%20Code%20in%20SQL%20Server%20Management%20Studio,by%20'CTRL%2BC'.)
- SQL - [Comparison Operators (Equal, Not Equal, Less than, Grater than)](https://www.tutlane.com/tutorial/sql-server/sql-comparison-operators)
- SQL - [Delete](https://www.w3schools.com/sql/sql_delete.asp)
- SQL - [INSERT INTO Syntax](https://www.w3schools.com/sql/sql_insert.asp)
- SQL - [Writing Loops](https://www.wiseowl.co.uk/blog/s348/loops-in-sql.htm)
- SQL - [Iterate Through Array Of Data In SQL Query](https://www.c-sharpcorner.com/article/iterate-through-array-of-data-in-sql-query/)
- SQL - [Getting the current system date and time](https://docs.microsoft.com/en-us/sql/t-sql/functions/getdate-transact-sql?view=sql-server-ver16)
- SQL - [Set Operators - EXCEPT and INTERSECT](https://docs.microsoft.com/en-us/sql/t-sql/language-elements/set-operators-except-and-intersect-transact-sql?view=sql-server-ver16)
- SQL - [COUNT() function with distinct clause](https://www.w3resource.com/sql/aggregate-functions/count-with-distinct.php)
- SQL - [How to Count Distinct Values in SQL: A Comprehensive Guide](https://www.sql-easy.com/learn/how-to-count-distinct-values-in-sql/#google_vignette)
- SQL - [Server PRINT and SQL Server RAISERROR statements](https://www.sqlshack.com/sql-server-print-and-sql-server-raiserror-statements/)
- SQL - [COUNT rows with user defined column heading](https://www.w3resource.com/sql/aggregate-functions/count-function.php)
- SQL - [Select Top N or Top N Random Rows](https://www.kodyaz.com/articles/sql-select-top-query.aspx)
- SQL - [How to Join 3 Tables (or More)](https://learnsql.com/blog/how-to-join-3-tables-or-more-in-sql/)
- SQL - [Create table with primary_key](https://learnsql.com/cookbook/how-to-create-a-primary-key-in-sql/)
- SQL - [How to select multiple columns but only group by one?](https://dba.stackexchange.com/questions/71887/how-to-select-multiple-columns-but-only-group-by-one)
- SQL - [How to Concatenate Multiple Rows into One Column in MySQL](https://ubiq.co/database-blog/concatenate-multiple-rows-one-column-mysql/#:~:text=In%20this%20case%2C%20we%20use,multiple%20rows%20into%20one%20column.&text=GROUP_CONCAT%20concatenates%20all%20non%2Dnull,add%20DISTINCT%20in%20your%20query.)
- SQL - [SQL Group with Most Recent Record Each](https://travishorn.com/sql-group-with-most-recent-record-each)
- SQL - [SQL Group By and Count on two columns](https://stackoverflow.com/questions/32901031/sql-group-by-and-count-on-two-columns)
- Nodejs - [Install Windows](https://www.guru99.com/download-install-node-js.html), if you want an specific version go [here](https://stackoverflow.com/questions/33849714/how-to-install-older-version-of-node-js-on-windows), and for mac go [here](https://medium.com/@georgeenathomas/3-step-process-to-downgrade-node-version-using-homebrew-bc0b0a72ae27) 
- Nodejs vs [JavaScript](https://www.knowledgehut.com/blog/web-development/node-js-vs-javasript), if you have issues with npm SELF_SIGNED_CERT_IN_CHAIN on Azure go [here](https://stackoverflow.com/questions/22099098/npm-self-signed-cert-in-chain-on-azure)
- JavaScript - [Remove Duplicates from json array](https://stackoverflow.com/questions/23507853/remove-duplicate-objects-from-json-array)
- JavaScript - [How to make POST Requests with Axios](https://rapidapi.com/guides/post-requests-axios)
- JavaScript - [how to read local.settings.json configuration in index.js file](https://stackoverflow.com/questions/71127337/how-to-read-local-settings-json-configuration-in-index-js-file)
- Python - [Implementation HMAC-SHA1](https://gist.github.com/heskyji/5167567b64cb92a910a3), you can find more functions definitions [here](https://gist.github.com/binaryatrocity/7079332cab038da1394d) or [Cryptographic signature and verification of messages](http://pymotw.com/2/hmac/)
- Python - [encode()](https://stackoverflow.com/questions/2340319/python-3-1-1-string-to-hex)
- Python - [Asynchronous HTTP Requests](https://www.twilio.com/blog/asynchronous-http-requests-in-python-with-aiohttp), [example of post request](https://stackoverflow.com/questions/55250420/aiohttp-async-session-requests), [request Post with param data](https://stackoverflow.com/questions/15900338/python-request-post-with-param-data)

- AKS - [Understanding concepts and docker](https://geekflare.com/docker-vs-kubernetes/)

<img width="758" alt="image" src="https://github.com/brown9804/DevOps-Agile-Cloud_path/assets/24630902/52bc950c-bce2-47cc-8b62-1ca7355ee616">

<img width="733" alt="image" src="https://github.com/brown9804/DevOps-Agile-Cloud_path/assets/24630902/a4312875-2bcc-4b30-a02d-b603829849f8">

- AKS - [Choosing the Right Kubernetes Cluster Approach: Multi-tenancy vs. Multi-cluster](https://www.linkedin.com/pulse/choosing-right-kubernetes-cluster-approach-vs-mina-gobrial?trk=public_post_main-feed-card_reshare_feed-article-content), Difference Between multi-cluster, multi-master, multi-tenant & federated Kubernetes [click here](https://platform9.com/blog/difference-between-multi-cluster-multi-master-multi-tenant-federated-kubernetes/)

<img width="958" alt="image" src="https://github.com/brown9804/DevOps-Agile-Cloud_path/assets/24630902/7cc8c40f-3c47-4b98-85b4-378a35dac9af">

<img width="906" alt="image" src="https://github.com/brown9804/DevOps-Agile-Cloud_path/assets/24630902/62c06ee7-d682-4870-8727-edda6eabe18c">

<img width="617" alt="image" src="https://github.com/brown9804/DevOps-Agile-Cloud_path/assets/24630902/14367694-c2df-4eaf-ae41-68ee088d3fec">

- AKS - [Understanding Multi-Cluster Kubernetes: Architecture, Benefits, and Challenges](https://traefik.io/glossary/understanding-multi-cluster-kubernetes/), Why would I want to use a multi-cluster architecture?, to understand that and difference between segmentation, and replication [click here](https://www.redhat.com/architect/multi-cluster-kubernetes-architecture)

<img width="1067" alt="image" src="https://github.com/brown9804/DevOps-Agile-Cloud_path/assets/24630902/6b16a8d4-f3f9-4843-bce7-e421630e04f3">

<img width="1098" alt="image" src="https://github.com/brown9804/DevOps-Agile-Cloud_path/assets/24630902/2a73bda1-4ea9-4d04-b3e7-99e9e8baee48">
