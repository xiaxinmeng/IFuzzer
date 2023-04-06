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

def test_singletons():
    for const in (None, False, True, Ellipsis, b'', frozenset()):
        with ConstantTests.subTest(const=const):
            value = ConstantTests.compile_constant(const)
            ConstantTests.assertIs(value, const)

ConstantTests = test_ast.ConstantTests()
test_singletons()
