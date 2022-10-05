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


class Emitter:
    def __init__(self, directory):
        self.directory = './' + directory
        self.providers = ''
        self.modules = ''
        self.variables = ''
        self.app = ''
        self.app_variables = ''

    def emit_provider(self, string):
        self.providers += string

    def emit_module(self, string):
        self.modules += string

    def emit_service(self, string):
        self.app += string

    def emit_variable(self, name, value=None):
        self.variables += _create_variable(name, value)

    def emit_app_variable(self, name, value=None):
        self.app_variables += _create_variable(name, value)

    def write_files(self):
        with open(self.directory + '/main.tf', 'w') as output_main:
            output_main.write(self.providers + self.modules)
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
