def replace_variable_by_value(data, load_balancer_resource):
    for key, value in data.items():
        if isinstance(value, dict):
            for group_key, group_value in value.items():
                if isinstance(group_value, int):
                    group_value = str(group_value)
                load_balancer_resource = load_balancer_resource.replace('#{' + group_key + '}', group_value)
        elif isinstance(value, int):
            value = str(value)
            load_balancer_resource = load_balancer_resource.replace('#{' + key + '}', value)
        elif isinstance(value, str):
            load_balancer_resource = load_balancer_resource.replace('#{' + key + '}', value)

    return load_balancer_resource


class LoadBalancer:
    def __init__(self, emitter):
        self.emitter = emitter

    def set_variables(self, key, value):
        if isinstance(value, dict):
            for group_key, group_value in value.items():
                self.emitter.emit_app_variable(group_key, group_value)
        elif isinstance(value, list):
            self.emitter.emit_app_array_variable(key, value)
        else:
            self.emitter.emit_app_variable(key, value)

    def get_load_balancer(self, data):
        self.set_variables('availability_zones', data.get('availability_zones'))
        self.set_variables('name-elb', data.get('name-elb'))
        self.set_variables('target', data.get('healthCheck').get('target'))
        load_balancer_resource = '''resource "aws_elb" "application" {
  name = "${var.name-elb}-${var.stage}"
  availability_zones = var.availability_zones

  listener {
    instance_port = #{instance_port}
    instance_protocol = "http"
    lb_port = #{lb_port}
    lb_protocol = "http"
  }

  health_check {
    healthy_threshold = #{healthy_threshold}
    unhealthy_threshold = #{unhealthy_threshold}
    timeout = #{timeout}
    target = var.target
    interval = #{interval}
  }

  instances = aws_instance.application.*.id
  cross_zone_load_balancing = true
  idle_timeout = #{idle_timeout}
  connection_draining = true
  connection_draining_timeout = #{connection_draining_timeout}

  tags = {
    Name = "var.name-elb-${var.stage}"
  }
}
'''
        return replace_variable_by_value(data, load_balancer_resource)
