def get_gci(name):
    return '''resource "google_compute_instance" "{0}" {{
  name = "${{var.gci_name}}-${{var.stage}}"
  zone = var.gcp_region
  machine_type = var.gci_type
  boot_disk {{
    initialize_params {{
      image = "debian-cloud/debian-11"
    }}
  }}
  network_interface {{
    network = "default"

    access_config {{
      // Ephemeral public IP
    }}
  }}
}}

'''.format(name)
