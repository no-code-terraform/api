from terraform.providers.provider import Provider


class Gcp(Provider):
    def __str__(self):
        return 'gcp'

    def provider(self, region, project):
        self.emitter.emit_variable('gcp_region', region)
        self.emitter.emit_variable('gcp_project', project)
        self.emitter.emit_provider('''provider "google" {
  credentials = file(var.gcp_service_account_file)

  project = var.gcp_project
  region  = var.gcp_region
}

''')

    def instance(self, data):
        todo = ''
        todo += ''

    def message(self, data):
        todo = ''
        todo += ''

    def load_balancing(self, data):
        todo = ''
        todo += ''
