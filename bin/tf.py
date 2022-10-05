from terraform.compiler import Compiler
from terraform.emitter import Emitter
import json


def main(data):
    emitter = Emitter('terraform')
    compiler = Compiler(json.loads(data), emitter)

    compiler.program()
    emitter.write_files()

    return open('./terraform.zip', 'r')
