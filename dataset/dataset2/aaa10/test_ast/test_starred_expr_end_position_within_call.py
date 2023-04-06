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

def test_starred_expr_end_position_within_call():
    node = ast.parse('f(*[0, 1])')
    starred_expr = node.body[0].value.args[0]
    ASTHelpers_Test.assertEqual(starred_expr.end_lineno, 1)
    ASTHelpers_Test.assertEqual(starred_expr.end_col_offset, 9)

ASTHelpers_Test = test_ast.ASTHelpers_Test()
test_starred_expr_end_position_within_call()
