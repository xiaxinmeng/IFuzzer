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

def test_isinstance():
    AST_Tests.assertTrue(isinstance(ast.Num(42), ast.Num))
    AST_Tests.assertTrue(isinstance(ast.Num(4.2), ast.Num))
    AST_Tests.assertTrue(isinstance(ast.Num(4.2j), ast.Num))
    AST_Tests.assertTrue(isinstance(ast.Str('42'), ast.Str))
    AST_Tests.assertTrue(isinstance(ast.Bytes(b'42'), ast.Bytes))
    AST_Tests.assertTrue(isinstance(ast.NameConstant(True), ast.NameConstant))
    AST_Tests.assertTrue(isinstance(ast.NameConstant(False), ast.NameConstant))
    AST_Tests.assertTrue(isinstance(ast.NameConstant(None), ast.NameConstant))
    AST_Tests.assertTrue(isinstance(ast.Ellipsis(), ast.Ellipsis))
    AST_Tests.assertTrue(isinstance(ast.Constant(42), ast.Num))
    AST_Tests.assertTrue(isinstance(ast.Constant(4.2), ast.Num))
    AST_Tests.assertTrue(isinstance(ast.Constant(4.2j), ast.Num))
    AST_Tests.assertTrue(isinstance(ast.Constant('42'), ast.Str))
    AST_Tests.assertTrue(isinstance(ast.Constant(b'42'), ast.Bytes))
    AST_Tests.assertTrue(isinstance(ast.Constant(True), ast.NameConstant))
    AST_Tests.assertTrue(isinstance(ast.Constant(False), ast.NameConstant))
    AST_Tests.assertTrue(isinstance(ast.Constant(None), ast.NameConstant))
    AST_Tests.assertTrue(isinstance(ast.Constant(...), ast.Ellipsis))
    AST_Tests.assertFalse(isinstance(ast.Str('42'), ast.Num))
    AST_Tests.assertFalse(isinstance(ast.Num(42), ast.Str))
    AST_Tests.assertFalse(isinstance(ast.Str('42'), ast.Bytes))
    AST_Tests.assertFalse(isinstance(ast.Num(42), ast.NameConstant))
    AST_Tests.assertFalse(isinstance(ast.Num(42), ast.Ellipsis))
    AST_Tests.assertFalse(isinstance(ast.NameConstant(True), ast.Num))
    AST_Tests.assertFalse(isinstance(ast.NameConstant(False), ast.Num))
    AST_Tests.assertFalse(isinstance(ast.Constant('42'), ast.Num))
    AST_Tests.assertFalse(isinstance(ast.Constant(42), ast.Str))
    AST_Tests.assertFalse(isinstance(ast.Constant('42'), ast.Bytes))
    AST_Tests.assertFalse(isinstance(ast.Constant(42), ast.NameConstant))
    AST_Tests.assertFalse(isinstance(ast.Constant(42), ast.Ellipsis))
    AST_Tests.assertFalse(isinstance(ast.Constant(True), ast.Num))
    AST_Tests.assertFalse(isinstance(ast.Constant(False), ast.Num))
    AST_Tests.assertFalse(isinstance(ast.Constant(), ast.Num))
    AST_Tests.assertFalse(isinstance(ast.Constant(), ast.Str))
    AST_Tests.assertFalse(isinstance(ast.Constant(), ast.Bytes))
    AST_Tests.assertFalse(isinstance(ast.Constant(), ast.NameConstant))
    AST_Tests.assertFalse(isinstance(ast.Constant(), ast.Ellipsis))

    class S(str):
        pass
    AST_Tests.assertTrue(isinstance(ast.Constant(S('42')), ast.Str))
    AST_Tests.assertFalse(isinstance(ast.Constant(S('42')), ast.Num))

AST_Tests = test_ast.AST_Tests()
test_isinstance()
