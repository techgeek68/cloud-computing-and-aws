# Deploys an EC2 instance using Terraform

provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "demo_server" {
  ami           = "ami-0c94855ba95c71c99" # AMI ID for Amazon Linux 2 in us-east-1
  instance_type = "t2.micro"              # Instance type eligible for free tier
}