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

def test_base_classes():
    AST_Tests.assertTrue(issubclass(ast.For, ast.stmt))
    AST_Tests.assertTrue(issubclass(ast.Name, ast.expr))
    AST_Tests.assertTrue(issubclass(ast.stmt, ast.AST))
    AST_Tests.assertTrue(issubclass(ast.expr, ast.AST))
    AST_Tests.assertTrue(issubclass(ast.comprehension, ast.AST))
    AST_Tests.assertTrue(issubclass(ast.Gt, ast.AST))

AST_Tests = test_ast.AST_Tests()
test_base_classes()
