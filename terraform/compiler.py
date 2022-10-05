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
        data = services.get('instances')
        if data:
            for datum in data:
                emitter.instance(self.data['stages'], datum)
        data = services.get('messaging')
        if data:
            for datum in data:
                emitter.message(datum)
        data = services.get('loadBalancers')
        if data:
            for datum in data:
                emitter.load_balancing(datum)
