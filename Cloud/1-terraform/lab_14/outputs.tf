# This code includes 3 output variables: instance_name, instance_id, and instance_public_ip.

output "instance_name" {
  description = "The tag name for this instance"
  value       = var.instance_name
}

output "instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.app_server.id
}

output "instance_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.app_server.public_ip
}