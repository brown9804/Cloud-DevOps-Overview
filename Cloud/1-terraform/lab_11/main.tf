provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "vm" {
  ami           = "DUMMY_VALUE_AMI_ID"
  subnet_id     = "DUMMY_VALUE_SUBNET_ID"
  instance_type = "t3.micro"
  tags = {
    Name = "my-first-tf-node"
  }
}

# terraform {
#    backend "remote" {
#      organization = "<YOUR ORG NAME>"
#      workspaces {
#        name = "lab-migrate-state"
#      }
#    }

#    required_providers {
#       aws = {
#         source  = "hashicorp/aws"
#         version = "~> 3.27"
#       }
#    }
# }