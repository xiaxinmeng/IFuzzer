from ast import *
tree = Module(body=[
    Import(names=[alias(name='builtins', lineno=1, col_offset=0)], lineno=1, col_offset=0), 
    Import(names=[alias(name='traceback', lineno=0, col_offset=0)], lineno=0, col_offset=1)
], type_ignores=[])
compile(tree, "x", "exec", dont_inherit=True)