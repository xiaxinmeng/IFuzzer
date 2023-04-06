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

def test_get_docstring():
    tree = ast.parse("'docstring'\nx = 1")
    ASTHelpers_Test.assertEqual(ast.get_docstring(tree), 'docstring')

ASTHelpers_Test = test_ast.ASTHelpers_Test()
test_get_docstring()
