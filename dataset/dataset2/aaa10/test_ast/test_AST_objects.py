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

def test_AST_objects():
    x = ast.AST()
    AST_Tests.assertEqual(x._fields, ())
    x.foobar = 42
    AST_Tests.assertEqual(x.foobar, 42)
    AST_Tests.assertEqual(x.__dict__['foobar'], 42)
    with AST_Tests.assertRaises(AttributeError):
        x.vararg
    with AST_Tests.assertRaises(TypeError):
        ast.AST(2)

AST_Tests = test_ast.AST_Tests()
test_AST_objects()
