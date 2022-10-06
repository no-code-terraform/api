import argparse
from datetime import datetime
import json
import os

from api.domain.terraform.compiler import Compiler
from api.domain.terraform.emitter import Emitter

TF_STORAGE_DIR = os.path.dirname(os.path.realpath(__file__)) + '/storage/tf'


def main(tf_data: str, tf_name: str = None) -> None:
    if tf_name is None:
        tf_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    build_path = f'{TF_STORAGE_DIR}/{tf_name}'
    os.mkdir(build_path)

    emitter = Emitter(build_path)
    compiler = Compiler(json.loads(tf_data), emitter)

    compiler.program()
    emitter.write_files()

    return print(f'Create build in {build_path}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Test builder'
    )
    parser.add_argument(
        'tf_data',
        type=str,
        help='The tf schema in json',
    )
    parser.add_argument(
        '--tf_name',
        type=str,
        nargs='+',
        help='Build folder name',
    )

    data = vars(parser.parse_args())

    main(**data)
