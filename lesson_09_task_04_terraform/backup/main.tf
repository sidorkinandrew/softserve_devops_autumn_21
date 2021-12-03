terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "3.5.0"
    }
  }
}

provider "google" {
  credentials = file("tf-gcp-test.json")

  project = "integral-kiln-332520"
  region  = "us-central1"
  zone    = "us-central1-c"
}

resource "google_compute_network" "vpc_network" {
  name = "terraform-network"
}


resource "google_compute_instance" "vm_instance" {
  name         = "terraform-instance"
  machine_type = "e2-micro"
  tags         = ["web", "dev", "http-server", "https-server"]

  boot_disk {
    initialize_params {
      image = "ubuntu-2004-focal-v20210927"
    }
  }

  metadata = {
    ssh-keys = "${var.gce_ssh_user}:${file(var.gce_ssh_key_file)}"
  }

  metadata_startup_script = "${data.template_file.gce_start.rendered}"

  network_interface {
    network = "default"
    access_config {
    }
  }
}


output "nat_ip" {
  value = google_compute_instance.vm_instance.network_interface.0.access_config.0.nat_ip
}


variable "gce_ssh_user" {
  type    = string
  default = "ubuntu"
}

variable "gce_ssh_key_file" {
  type    = string
  default = "gce_ssh_user.pem.pub"
}


data "template_file" "gce_start" {
  template = "${file("./scripts/gce_start.sh")}"
  vars = {
    address = "some value"
  }
}