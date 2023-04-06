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

def test_literal_eval_malformed_lineno():
    msg = 'malformed node or string on line 3:'
    with ASTHelpers_Test.assertRaisesRegex(ValueError, msg):
        ast.literal_eval("{'a': 1,\n'b':2,\n'c':++3,\n'd':4}")
    node = ast.UnaryOp(ast.UAdd(), ast.UnaryOp(ast.UAdd(), ast.Constant(6)))
    ASTHelpers_Test.assertIsNone(getattr(node, 'lineno', None))
    msg = 'malformed node or string:'
    with ASTHelpers_Test.assertRaisesRegex(ValueError, msg):
        ast.literal_eval(node)

ASTHelpers_Test = test_ast.ASTHelpers_Test()
test_literal_eval_malformed_lineno()
