terraform {
  required_providers {
    aws = {
        source = "hashcorp/aws"
    }
  }
}

provider "aws" {
    profile = "default"
    region = "ap-southeast-1"
}

resource "aws_instance" "name" {
  name = ""
  ami_id = ""
  instance_type = ""
}