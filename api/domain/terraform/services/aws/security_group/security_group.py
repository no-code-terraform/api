from string import Template

from api.domain.terraform.services.aws.security_group.rule import Rule


class MyTemplate(Template):
    delimiter = "#"


class SecurityGroup:
    def __init__(self, type):
        self.rules = []
        self.type = type

    def open_security_group(self):
        pass

    def default_instance_rule(self):
        ssh_rule = Rule(22, 22)
        http_rule = Rule(80, 80)
        https_rule = Rule(443, 443)
        self.rules.append(ssh_rule.get_rule())
        self.rules.append(http_rule.get_rule())
        self.rules.append(https_rule.get_rule())

    def add_rule(self, rule):
        self.rules.append(rule)

    def get_security_group(self):
        final = ""
        begin_template = MyTemplate('''resource "aws_security_group" "#type" {
    name        =   "${var.stage}--#type"
    description =   "Allow inbound traffic"

''')
        ingress_template = MyTemplate('''
    ingress {
        from_port   = #from
        to_port     = #to
        protocol    = #protocol
        cidr_blocks = #block
      }
''')
        end_template = MyTemplate('''
    egress {
        from_port   = 0
        to_port     = 0
        protocol    = "-1"
        cidr_blocks = ["0.0.0.0/0"]
  }

    tags = {
        Name = "${var.stage}-application"
    }
}

''')
        final += begin_template.substitute({'type': self.type})
        for rule in self.rules:
            final += ingress_template.substitute(rule)
        final += end_template.substitute()
        return final
