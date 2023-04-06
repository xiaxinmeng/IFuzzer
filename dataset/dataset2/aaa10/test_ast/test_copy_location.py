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

def test_copy_location():
    src = ast.parse('1 + 1', mode='eval')
    src.body.right = ast.copy_location(ast.Num(2), src.body.right)
    ASTHelpers_Test.assertEqual(ast.dump(src, include_attributes=True), 'Expression(body=BinOp(left=Constant(value=1, lineno=1, col_offset=0, end_lineno=1, end_col_offset=1), op=Add(), right=Constant(value=2, lineno=1, col_offset=4, end_lineno=1, end_col_offset=5), lineno=1, col_offset=0, end_lineno=1, end_col_offset=5))')
    src = ast.Call(col_offset=1, lineno=1, end_lineno=1, end_col_offset=1)
    new = ast.copy_location(src, ast.Call(col_offset=None, lineno=None))
    ASTHelpers_Test.assertIsNone(new.end_lineno)
    ASTHelpers_Test.assertIsNone(new.end_col_offset)
    ASTHelpers_Test.assertEqual(new.lineno, 1)
    ASTHelpers_Test.assertEqual(new.col_offset, 1)

ASTHelpers_Test = test_ast.ASTHelpers_Test()
test_copy_location()
