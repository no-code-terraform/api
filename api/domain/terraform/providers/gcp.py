from api.domain.terraform.providers.provider import Provider
from api.domain.terraform.services.pub_sub import get_sub


class Gcp(Provider):
    def __str__(self):
        return 'gcp'

    def provider(self, region, project):
        self.emitter.emit_variable('gcp_region', region)
        self.emitter.emit_variable('gcp_project', project)
        self.emitter.emit_variable('gcp_service_account_file')
        self.emitter.emit_provider('''provider "google" {
  credentials = file(var.gcp_service_account_file)

  project = var.gcp_project
  region  = var.gcp_region
}

''')

    def gci(self, data, stages):
        self.emitter.emit_module(stages, {
            'gci_name': '"' + data.get('gci_name') + '"',
            'gci_type': '"' + data.get('gci_type') + '"',
        })
        self.emitter.emit_service(('''resource "google_compute_instance" "{0}" {{
  name = var.gci_name
  machine_type = var.gci_type
  boot_disk {{
    initialize_params {{
      image = "debian-cloud/debian-9"
    }}
  }}
  network_interface {{
    network = "default"

    access_config {{
      // Ephemeral public IP
    }}
  }}
}}

''').format(data.get('gci_name')))

    def pub_sub(self, data, stages):
        self.emitter.emit_service(get_sub(data.get('topic')))
