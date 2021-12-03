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