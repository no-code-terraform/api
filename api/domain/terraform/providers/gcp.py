from api.domain.terraform.providers.provider import Provider
from api.domain.terraform.services.gcp.pub_sub.pub_sub import get_sub
from api.domain.terraform.services.gcp.gci.google_compute_instance import get_gci


class Gcp(Provider):
    def __str__(self):
        return 'gcp'

    def provider(self, region, project):
        self.emitter.emit_variable('gcp_region', region)
        self.emitter.emit_variable('gcp_project', project)
        self.emitter.emit_provider('''provider "google" {
  project = var.gcp_project
  region  = var.gcp_region
}

''')

    def gci(self, data, stages):
        self.emitter.emit_module(stages, {
            'gci_name': '"' + data.get('gci_name') + '"',
            'gci_type': '"' + data.get('gci_type') + '"',
            'gcp_region': '"' + data.get('region') + '"',

        })
        self.emitter.emit_service(self.__str__(), get_gci(data.get('gci_name')))

    def pubsub(self, data, stages):
        self.emitter.emit_service(self.__str__(), get_sub(data.get('topic')))
