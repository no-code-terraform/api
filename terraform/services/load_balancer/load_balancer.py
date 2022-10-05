class LoadBalancer:
    def __init__(self, emitter):
        self.emitter = emitter

    def set_variables(self, data):
        for key, values in data.items():
            if isinstance(values, dict):
                for group_key, group_value in values.items():
                    self.emitter.emit_app_variable(group_key, group_value)
            # elif isinstance(values, list):
            #    self.emitter.emit_app_variable(key, values)
            elif isinstance(values, str):
                self.emitter.emit_app_variable(key, values)

    @staticmethod
    def generate_load_balancer():
        return '''resource "aws_elb" "application" {
  name = var.name-elb
  availability_zones = var.availability_zones

  listener {
    instance_port = var.instance_port
    instance_protocol = "http"
    lb_port = var.lb_port
    lb_protocol = "http"
  }

  health_check {
    healthy_threshold = 2
    unhealthy_threshold = 2
    timeout = 3
    target = var.target
    interval = 30
  }

  instances = aws_instance.application.*.id
  cross_zone_load_balancing = true
  idle_timeout = 400
  connection_draining = true
  connection_draining_timeout = 400

  tags = {
    Name = var.name-elb
  }
}
'''
