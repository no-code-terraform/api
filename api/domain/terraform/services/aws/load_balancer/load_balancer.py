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
        self.set_variables('availability_zones_' + data.get('instances'), data.get('availability_zones'))
        self.set_variables('name-elb_' + data.get('instances'), data.get('name-elb'))
        self.set_variables('target_' + data.get('instances'), data.get('healthCheck').get('target'))
        load_balancer_resource = '''resource "aws_elb" "application" {
  name = "${var.name-elb_#{instances}}-${var.stage}"
  availability_zones = var.availability_zones_#{instances}

  listener {
    instance_port = #{instance_port}
    instance_protocol = "http"
    lb_port = #{lb_port}
    lb_protocol = "http"
  }

  health_check {
    healthy_threshold = 2
    unhealthy_threshold = 2
    timeout = 3
    target = var.target_#{instances}
    interval = 30
  }

  instances = aws_instance.#{instances}.*.id
  cross_zone_load_balancing = true
  idle_timeout = #{idle_timeout}
  connection_draining = true
  connection_draining_timeout = 400

  tags = {
    Name = "var.name-elb#{instances}-${var.stage}"
  }
}
'''
        return replace_variable_by_value(data, load_balancer_resource)
