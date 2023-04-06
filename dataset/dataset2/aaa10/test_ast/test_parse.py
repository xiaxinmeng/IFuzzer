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

def test_parse():
    a = ast.parse('foo(1 + 1)')
    b = compile('foo(1 + 1)', '<unknown>', 'exec', ast.PyCF_ONLY_AST)
    ASTHelpers_Test.assertEqual(ast.dump(a), ast.dump(b))

ASTHelpers_Test = test_ast.ASTHelpers_Test()
test_parse()
