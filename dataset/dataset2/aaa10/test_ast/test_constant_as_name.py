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

def test_constant_as_name():
    for constant in ('True', 'False', 'None'):
        expr = ast.Expression(ast.Name(constant, ast.Load()))
        ast.fix_missing_locations(expr)
        with AST_Tests.assertRaisesRegex(ValueError, f"Name node can't be used with '{constant}' constant"):
            compile(expr, '<test>', 'eval')

AST_Tests = test_ast.AST_Tests()
test_constant_as_name()
