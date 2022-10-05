from terraform.compiler import Compiler
from terraform.emitter import Emitter
import json


def main(data):
    emitter = Emitter('terraform')
    compiler = Compiler(json.loads(data), emitter)

    compiler.program()
    emitter.write_files()

    return open('./tfmaker.zip', 'r')


if __name__ == "__main__":
    print(add(2, 3))
