import ast
import builtins
import dis
import os
import sys
import types
import unittest
import warnings
import weakref
from textwrap import dedent
from test import support
import pickle

import unicodedata
import _ast as ast1
import _ast as ast2
import _ast
import test_ast

def test_subinterpreter():
    code = dedent("\n            import _ast\n            import ast\n            import gc\n            import sys\n            import types\n\n            # Create _ast.AST subclasses instances and call PyAST_Check()\n            ast_tree = compile('x+1', '<string>', 'eval',\n                               flags=ast.PyCF_ONLY_AST)\n            code = compile(ast_tree, 'string', 'eval')\n            if not isinstance(code, types.CodeType):\n                raise AssertionError\n\n            # Unloading the _ast module must not crash.\n            del ast, _ast\n            del sys.modules['ast'], sys.modules['_ast']\n            gc.collect()\n        ")
    res = support.run_in_subinterp(code)
    ModuleStateTests.assertEqual(res, 0)

ModuleStateTests = test_ast.ModuleStateTests()
test_subinterpreter()
