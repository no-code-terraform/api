from terraform.compiler import Compiler
from terraform.emitter import Emitter
from pathlib import Path
import json

terraform_dir = str(Path(__file__).resolve().parent.parent) + '/terraform'


def main():
    with open('../tf-schema.json', 'r') as input_file:
        data = input_file.read()

    emitter = Emitter(terraform_dir + '/build')
    compiler = Compiler(json.loads(data), emitter)

    compiler.program()
    emitter.write_files()

    return open(terraform_dir + '/build.zip', 'r')


if __name__ == "__main__":
    print(main())
