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

def test_arguments():
    x = ast.arguments()
    AST_Tests.assertEqual(x._fields, ('posonlyargs', 'args', 'vararg', 'kwonlyargs', 'kw_defaults', 'kwarg', 'defaults'))
    with AST_Tests.assertRaises(AttributeError):
        x.args
    AST_Tests.assertIsNone(x.vararg)
    x = ast.arguments(*range(1, 8))
    AST_Tests.assertEqual(x.args, 2)
    AST_Tests.assertEqual(x.vararg, 3)

AST_Tests = test_ast.AST_Tests()
test_arguments()
