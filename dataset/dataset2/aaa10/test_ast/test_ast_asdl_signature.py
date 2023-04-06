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

def test_ast_asdl_signature():
    AST_Tests.assertEqual(ast.withitem.__doc__, 'withitem(expr context_expr, expr? optional_vars)')
    AST_Tests.assertEqual(ast.GtE.__doc__, 'GtE')
    AST_Tests.assertEqual(ast.Name.__doc__, 'Name(identifier id, expr_context ctx)')
    AST_Tests.assertEqual(ast.cmpop.__doc__, 'cmpop = Eq | NotEq | Lt | LtE | Gt | GtE | Is | IsNot | In | NotIn')
    expressions = [f'     | {node.__doc__}' for node in ast.expr.__subclasses__()]
    expressions[0] = f'expr = {ast.expr.__subclasses__()[0].__doc__}'
    AST_Tests.assertCountEqual(ast.expr.__doc__.split('\n'), expressions)

AST_Tests = test_ast.AST_Tests()
test_ast_asdl_signature()
