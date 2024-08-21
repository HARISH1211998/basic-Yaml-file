#terraform Block 
terraform {
  required_providers {
    aws = {
        source = "hashcorp/aws"
    }
  }
}

# Provider Block 
provider "aws" {
    profile = "default"
    region = "ap-southeast-1"
}

# Variable Block
variable "ec2_instance_type" {
  type = list(string)
  default = [ "t2.medium", "t2.micro" ]
}

# Data Source Block
data "aws_vpc" "canton_vpc" {
  name = "tag:name"
  values = ["canton"]
}

# OutPut Block
output "vpc_id" {
  value = data.aws_vpc.canton_vpc.id
}

# Resources Block
resource "aws_instance" "test_2ec2_instances" {
  name = ""
  ami_id = ""

  # For Each
  for_each = var.ec2_instance_type
  instance_type = each.value
  vpc_id = data.canton_vpc.vpc_id
  count = 2
  # Count Index
  tags = {
    "Name" = "canton-${count.index}"
  }

  # Provisioner with local Execution
  provisioner "local-exec" {
    command = "echo ${self.private_ip} >> private_ips.txt"
  }

  # Provisioner with Remote Execution
  provisioner "remote-exec" {
    inline = [
      "sudo apt-get update",
      "sudo apt-get install -y nginx"
    ]
    connection {
      type = "ssh"
      user = "XXXXXX"
      private_key = file("~/.ssh/id_rsa")
      host = self.public_ip
    }
  }
}    

output "instance_ids" {
  value = { for k, v in aws_instance.test_2ec2_instances : k => v.id }
}