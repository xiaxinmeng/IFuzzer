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

def test_invalid_sum():
    pos = dict(lineno=2, col_offset=3)
    m = ast.Module([ast.Expr(ast.expr(**pos), **pos)], [])
    with AST_Tests.assertRaises(TypeError) as cm:
        compile(m, '<test>', 'exec')
    AST_Tests.assertIn('but got <ast.expr', str(cm.exception))

AST_Tests = test_ast.AST_Tests()
test_invalid_sum()
