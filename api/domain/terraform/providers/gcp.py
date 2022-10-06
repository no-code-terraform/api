from api.domain.terraform.providers.provider import Provider
from api.domain.terraform.services.pub_sub import get_sub
from api.domain.terraform.services.gci.google_compute_instance import get_gci


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
        self.emitter.emit_service(get_gci(data.get('gci_name')))

    def pubsub(self, data, stages):
        self.emitter.emit_service(get_sub(data.get('topic')))
