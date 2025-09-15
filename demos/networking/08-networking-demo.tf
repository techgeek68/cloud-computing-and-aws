# Terraform script for creating a basic AWS VPC

provider "aws" {
  region = "us-east-1"
}

resource "aws_vpc" "demo_vpc" {
  cidr_block = "10.0.0.0/16" # CIDR block for the new VPC
}