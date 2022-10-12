from api.domain.terraform.providers.provider import Provider
from api.domain.terraform.services.aws.load_balancer.load_balancer import LoadBalancer
from api.domain.terraform.services.aws.security_group.security_group import SecurityGroup
from api.domain.terraform.services.aws.instance.instance import get_instance


class Aws(Provider):
    def __str__(self):
        return 'aws'

    def provider(self, region, project):
        self.emitter.emit_variable('aws_region', region)
        self.emitter.emit_variable('ssh_public_key_file')
        self.emitter.emit_provider('''provider "aws" {
  version = "~> 2.0"
  region  = var.aws_region
}

resource "aws_key_pair" "app-key" {
  key_name = "app"
  public_key = file(var.ssh_public_key_file)
}

''')

    def ec2(self, data, stages):
        self.emitter.emit_module(stages, {
            'instance_type_' + data.get('name'): '"' + data.get('instance_type') + '"',
            'instance_ami_' + data.get('name'): '"' + data.get('ami') + '"',
            'instance_count_' + data.get('name'): data.get('count'),
            'instance_key_name': 'aws_key_pair.app-key.key_name',
        })
        self.emitter.emit_service(self.__str__(), get_instance(data.get('name')))
        self._security_group(data.get('name'), data.get('ports'))

    def _security_group(self, type, ports):
        sg = SecurityGroup(type)
        sg.default_instance_rule()
        self.emitter.emit_service(self.__str__(), sg.get_security_group())

    def elb(self, data, stages):
        self.emitter.emit_service(
            self.__str__(),
            LoadBalancer(self.emitter).get_load_balancer(data)
        )
