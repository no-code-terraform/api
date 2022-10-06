from terraform.providers.provider import Provider
from terraform.services.load_balancer.load_balancer import LoadBalancer
from terraform.services.security_group.security_group import SecurityGroup


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
            'instance_type': '"' + data.get('instance_type') + '"',
            'instance_ami': '"' + data.get('ami') + '"',
            'instance_count': data.get('count'),
            'instance_key_name': 'aws_key_pair.app-key.key_name',
        })
        self.emitter.emit_service(('''resource "aws_instance" "{0}" {{
  ami = var.instance_ami
  instance_type = var.instance_type
  key_name = var.instance_key_name

  count = var.instance_count

  security_groups = [aws_security_group.{0}.name]

  tags = {{
    Name = "${{var.stage}}-{0}"
    component = "{0}"
    stage = var.stage
  }}
}}

''').format(data.get('name')))
        self._security_group(data.get('name'), data.get('ports'))

    def _security_group(self, type, ports):
        sg = SecurityGroup(type)
        sg.default_instance_rule()
        self.emitter.emit_service(sg.get_security_group())

    def elb(self, data, stages):
        self.emitter.emit_service(
            LoadBalancer(self.emitter).get_load_balancer(data)
        )
