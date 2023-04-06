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

def test_increment_lineno():
    src = ast.parse('1 + 1', mode='eval')
    ASTHelpers_Test.assertEqual(ast.increment_lineno(src, n=3), src)
    ASTHelpers_Test.assertEqual(ast.dump(src, include_attributes=True), 'Expression(body=BinOp(left=Constant(value=1, lineno=4, col_offset=0, end_lineno=4, end_col_offset=1), op=Add(), right=Constant(value=1, lineno=4, col_offset=4, end_lineno=4, end_col_offset=5), lineno=4, col_offset=0, end_lineno=4, end_col_offset=5))')
    src = ast.parse('1 + 1', mode='eval')
    ASTHelpers_Test.assertEqual(ast.increment_lineno(src.body, n=3), src.body)
    ASTHelpers_Test.assertEqual(ast.dump(src, include_attributes=True), 'Expression(body=BinOp(left=Constant(value=1, lineno=4, col_offset=0, end_lineno=4, end_col_offset=1), op=Add(), right=Constant(value=1, lineno=4, col_offset=4, end_lineno=4, end_col_offset=5), lineno=4, col_offset=0, end_lineno=4, end_col_offset=5))')
    src = ast.Call(func=ast.Name('test', ast.Load()), args=[], keywords=[], lineno=1)
    ASTHelpers_Test.assertEqual(ast.increment_lineno(src).lineno, 2)
    ASTHelpers_Test.assertIsNone(ast.increment_lineno(src).end_lineno)

ASTHelpers_Test = test_ast.ASTHelpers_Test()
test_increment_lineno()
