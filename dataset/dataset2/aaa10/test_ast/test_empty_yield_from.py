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

def test_empty_yield_from():
    empty_yield_from = ast.parse('def f():\n yield from g()')
    empty_yield_from.body[0].body[0].value.value = None
    with AST_Tests.assertRaises(ValueError) as cm:
        compile(empty_yield_from, '<test>', 'exec')
    AST_Tests.assertIn("field 'value' is required", str(cm.exception))

AST_Tests = test_ast.AST_Tests()
test_empty_yield_from()
