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

def test_dump():
    node = ast.parse('spam(eggs, "and cheese")')
    ASTHelpers_Test.assertEqual(ast.dump(node), "Module(body=[Expr(value=Call(func=Name(id='spam', ctx=Load()), args=[Name(id='eggs', ctx=Load()), Constant(value='and cheese')], keywords=[]))], type_ignores=[])")
    ASTHelpers_Test.assertEqual(ast.dump(node, annotate_fields=False), "Module([Expr(Call(Name('spam', Load()), [Name('eggs', Load()), Constant('and cheese')], []))], [])")
    ASTHelpers_Test.assertEqual(ast.dump(node, include_attributes=True), "Module(body=[Expr(value=Call(func=Name(id='spam', ctx=Load(), lineno=1, col_offset=0, end_lineno=1, end_col_offset=4), args=[Name(id='eggs', ctx=Load(), lineno=1, col_offset=5, end_lineno=1, end_col_offset=9), Constant(value='and cheese', lineno=1, col_offset=11, end_lineno=1, end_col_offset=23)], keywords=[], lineno=1, col_offset=0, end_lineno=1, end_col_offset=24), lineno=1, col_offset=0, end_lineno=1, end_col_offset=24)], type_ignores=[])")

ASTHelpers_Test = test_ast.ASTHelpers_Test()
test_dump()
