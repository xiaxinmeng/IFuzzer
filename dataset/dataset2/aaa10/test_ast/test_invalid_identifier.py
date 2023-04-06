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

def test_invalid_identifier():
    m = ast.Module([ast.Expr(ast.Name(42, ast.Load()))], [])
    ast.fix_missing_locations(m)
    with AST_Tests.assertRaises(TypeError) as cm:
        compile(m, '<test>', 'exec')
    AST_Tests.assertIn('identifier must be of type str', str(cm.exception))

AST_Tests = test_ast.AST_Tests()
test_invalid_identifier()
