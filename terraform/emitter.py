import shutil
import os


def _create_variable(name, value=None):
    data = 'variable "' + name + '''" {
  type = string'''
    if value:
        data += '''
  default = "''' + value + '"'
    data += '''
}

'''
    return data


def _create_array_variables(name, value):
    data = 'variable "' + name + '''" {
  type = list(string)'''
    if value:
        data += '''
  default = ''' + value + ''
    data += '''
}

'''
    return data


class Emitter:
    def __init__(self, directory):
        self.directory = directory
        self.providers = ''
        self.modules = {}
        self.modules_stage = []
        self.variables = ''
        self.app = ''
        self.app_variables = ''

    def emit_provider(self, string):
        self.providers += string

    def emit_module(self, stages, modules):
        self.modules_stage = stages
        self.modules |= modules

    def _emit_module(self):
        module_value = ''
        module = ''
        self.emit_app_variable('stage')
        for name in self.modules:
            self.emit_app_variable(name)
            module_value += ('''
  {0} = {1}''').format(name, self.modules[name])
        for stage in self.modules_stage:
            module += ('''module  "{0}" {{
  source = "./application"

  stage = "{0}"''').format(stage)
            module += module_value
            module += '''
}

'''
        return module

    def emit_service(self, string):
        self.app += string

    def emit_variable(self, name, value=None):
        self.variables += _create_variable(name, value)

    def emit_app_variable(self, name, value=None):
        self.app_variables += _create_variable(name, value)

    def emit_app_array_variable(self, name, values):
        array_string = '['
        for value in values:
            value = str(value)
            array_string += '"' + value + '",'
        if array_string.endswith('",'):
            array_string = array_string[:-1]
            array_string += ']'
        self.app_variables = _create_array_variables(name, array_string)

    def write_files(self):
        with open(self.directory + '/main.tf', 'w') as output_main:
            output_main.write(self.providers + self._emit_module())
        with open(self.directory + '/variables.tf', 'w') as output_variable:
            output_variable.write(self.variables)
        path = self.directory + '/application/'
        if not os.path.exists(path):
            os.mkdir(path)
        with open(path + 'main.tf', 'w') as output_main:
            output_main.write(self.app)
        with open(path + 'variables.tf', 'w') as output_variable:
            output_variable.write(self.app_variables)
        shutil.make_archive(self.directory, 'zip', self.directory)
