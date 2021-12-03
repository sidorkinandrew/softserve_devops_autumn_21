terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "3.5.0"
    }
  }
}

provider "google" {
  credentials = file(".ssh/tf-gcp-test.json")

  project = "integral-kiln-332520"
  region  = "us-central1"
  zone    = "us-central1-c"
}
