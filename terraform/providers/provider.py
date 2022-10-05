class Provider:
    def __init__(self, emitter):
        self.emitter = emitter

    def module(self, stages, instance_type, ami, count):
        self.emitter.emit_app_variable('instance_ami')
        self.emitter.emit_app_variable('instance_type')
        self.emitter.emit_app_variable('instance_key_name')
        self.emitter.emit_app_variable('instance_count')
        self.emitter.emit_app_variable('stage')
        for stage in stages:
            self.emitter.emit_module(('''module  "{0}" {{
  source = "./application"

  instance_type = "{1}"
  instance_ami = "{2}"
  instance_count = {3}
  instance_key_name = aws_key_pair.app-key.key_name
  stage = "{4}"
}}

''').format(stage, instance_type, ami, count, stage))
