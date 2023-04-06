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

def test_realtype():
    AST_Tests.assertEqual(type(ast.Num(42)), ast.Constant)
    AST_Tests.assertEqual(type(ast.Num(4.25)), ast.Constant)
    AST_Tests.assertEqual(type(ast.Num(4.25j)), ast.Constant)
    AST_Tests.assertEqual(type(ast.Str('42')), ast.Constant)
    AST_Tests.assertEqual(type(ast.Bytes(b'42')), ast.Constant)
    AST_Tests.assertEqual(type(ast.NameConstant(True)), ast.Constant)
    AST_Tests.assertEqual(type(ast.NameConstant(False)), ast.Constant)
    AST_Tests.assertEqual(type(ast.NameConstant(None)), ast.Constant)
    AST_Tests.assertEqual(type(ast.Ellipsis()), ast.Constant)

AST_Tests = test_ast.AST_Tests()
test_realtype()
