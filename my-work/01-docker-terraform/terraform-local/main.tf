terraform {
  required_providers {
    local = {
      source = "hashicorp/local"
    }
  }
}

variable "message" {
  type    = string
  default = "Hello from Terraform"
}

resource "local_file" "hello" {
  filename = "${path.module}/hello.txt"
  content  = var.message
}
