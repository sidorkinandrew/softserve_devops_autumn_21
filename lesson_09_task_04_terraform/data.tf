data "template_file" "gce_start" {
  template = "${file("./scripts/gce_start.sh")}"
  vars = {
    address = "some value"
  }
}