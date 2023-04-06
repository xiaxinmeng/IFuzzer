import sys
PyCF_ONLY_AST = 1024
tree = compile("x+y", "filename", "exec", PyCF_ONLY_AST)

import _ast
assert PyCF_ONLY_AST == _ast.PyCF_ONLY_AST

compile(tree, "filename", "exec")
del sys.modules['_ast']

import _ast
compile(tree, "filename", "exec")