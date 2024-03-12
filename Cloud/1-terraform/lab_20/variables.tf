# variables.tf

variable region {
  description = "The AWS region your resources will be deployed"
}

variable name {
  description = "The operator name running this configuration"
}

variable ami {
  description = "The ami for the configuration"
}

variable subnet_id {
  description = "The subnet_id for the configuration"
}
