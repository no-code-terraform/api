from terraform.providers.aws import Aws
from terraform.providers.gcp import Gcp


class Compiler:
    def __init__(self, data, emitter):
        self.data = data
        self.providers = {
            'aws': Aws(emitter),
            'gcp': Gcp(emitter),
        }

    def program(self):
        for provider in self.data['providers']:
            data = self.data['providers'][provider]
            emitter = self.providers[provider]
            emitter.provider(data['region'], data.get('project'))
            self._services(emitter, data.get('services'))

    def _services(self, emitter, services):
        for service in services:
            service_call = getattr(emitter, service, None)
            if callable(service_call):
                for data in services[service]:
                    service_call(data, self.data['stages'])
