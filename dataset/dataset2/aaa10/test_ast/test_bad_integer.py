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

def test_bad_integer():
    body = [ast.ImportFrom(module='time', names=[ast.alias(name='sleep')], level=None, lineno=None, col_offset=None)]
    mod = ast.Module(body, [])
    with ASTHelpers_Test.assertRaises(ValueError) as cm:
        compile(mod, 'test', 'exec')
    ASTHelpers_Test.assertIn('invalid integer value: None', str(cm.exception))

ASTHelpers_Test = test_ast.ASTHelpers_Test()
test_bad_integer()
