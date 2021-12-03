variable "gce_ssh_user" {
  type    = string
  default = "ubuntu"
}

variable "gce_ssh_key_file" {
  type    = string
  default = ".ssh/gce_ssh_user.pem.pub"
}
