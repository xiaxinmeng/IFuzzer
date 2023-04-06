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

def test_get_docstring_none():
    ASTHelpers_Test.assertIsNone(ast.get_docstring(ast.parse('')))
    node = ast.parse('x = "not docstring"')
    ASTHelpers_Test.assertIsNone(ast.get_docstring(node))
    node = ast.parse('def foo():\n  pass')
    ASTHelpers_Test.assertIsNone(ast.get_docstring(node))
    node = ast.parse('class foo:\n  pass')
    ASTHelpers_Test.assertIsNone(ast.get_docstring(node.body[0]))
    node = ast.parse('class foo:\n  x = "not docstring"')
    ASTHelpers_Test.assertIsNone(ast.get_docstring(node.body[0]))
    node = ast.parse('class foo:\n  def bar(ASTHelpers_Test): pass')
    ASTHelpers_Test.assertIsNone(ast.get_docstring(node.body[0]))
    node = ast.parse('def foo():\n  pass')
    ASTHelpers_Test.assertIsNone(ast.get_docstring(node.body[0]))
    node = ast.parse('def foo():\n  x = "not docstring"')
    ASTHelpers_Test.assertIsNone(ast.get_docstring(node.body[0]))
    node = ast.parse('async def foo():\n  pass')
    ASTHelpers_Test.assertIsNone(ast.get_docstring(node.body[0]))
    node = ast.parse('async def foo():\n  x = "not docstring"')
    ASTHelpers_Test.assertIsNone(ast.get_docstring(node.body[0]))

ASTHelpers_Test = test_ast.ASTHelpers_Test()
test_get_docstring_none()
