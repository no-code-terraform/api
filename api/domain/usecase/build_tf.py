from api.domain.terraform.compiler import Compiler
from api.domain.terraform.emitter import Emitter

def execute(
    tf_data: dict,
    tf_path: str,
) -> None:
    emitter = Emitter(tf_path)
    compiler = Compiler(tf_data, emitter)

    compiler.program()
    emitter.write_files()
