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

def test_string_kind():
    c = ast.parse('"x"', mode='eval').body
    ConstantTests.assertEqual(c.value, 'x')
    ConstantTests.assertEqual(c.kind, None)
    c = ast.parse('u"x"', mode='eval').body
    ConstantTests.assertEqual(c.value, 'x')
    ConstantTests.assertEqual(c.kind, 'u')
    c = ast.parse('r"x"', mode='eval').body
    ConstantTests.assertEqual(c.value, 'x')
    ConstantTests.assertEqual(c.kind, None)
    c = ast.parse('b"x"', mode='eval').body
    ConstantTests.assertEqual(c.value, b'x')
    ConstantTests.assertEqual(c.kind, None)

ConstantTests = test_ast.ConstantTests()
test_string_kind()
