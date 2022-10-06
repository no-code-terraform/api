def get_instance(name):
    return '''resource "aws_instance" "{0}" {{
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

'''.format(name)
