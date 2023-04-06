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

def test_fix_missing_locations():
    src = ast.parse('write("spam")')
    src.body.append(ast.Expr(ast.Call(ast.Name('spam', ast.Load()), [ast.Str('eggs')], [])))
    ASTHelpers_Test.assertEqual(src, ast.fix_missing_locations(src))
    ASTHelpers_Test.maxDiff = None
    ASTHelpers_Test.assertEqual(ast.dump(src, include_attributes=True), "Module(body=[Expr(value=Call(func=Name(id='write', ctx=Load(), lineno=1, col_offset=0, end_lineno=1, end_col_offset=5), args=[Constant(value='spam', lineno=1, col_offset=6, end_lineno=1, end_col_offset=12)], keywords=[], lineno=1, col_offset=0, end_lineno=1, end_col_offset=13), lineno=1, col_offset=0, end_lineno=1, end_col_offset=13), Expr(value=Call(func=Name(id='spam', ctx=Load(), lineno=1, col_offset=0, end_lineno=1, end_col_offset=0), args=[Constant(value='eggs', lineno=1, col_offset=0, end_lineno=1, end_col_offset=0)], keywords=[], lineno=1, col_offset=0, end_lineno=1, end_col_offset=0), lineno=1, col_offset=0, end_lineno=1, end_col_offset=0)], type_ignores=[])")

ASTHelpers_Test = test_ast.ASTHelpers_Test()
test_fix_missing_locations()
