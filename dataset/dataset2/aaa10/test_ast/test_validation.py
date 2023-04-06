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

def test_validation():
    with ConstantTests.assertRaises(TypeError) as cm:
        ConstantTests.compile_constant([1, 2, 3])
    ConstantTests.assertEqual(str(cm.exception), 'got an invalid type in Constant: list')

ConstantTests = test_ast.ConstantTests()
test_validation()
