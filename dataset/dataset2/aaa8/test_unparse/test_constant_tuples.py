import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_constant_tuples():
    UnparseTestCase.check_src_roundtrip(ast.Constant(value=(1,), kind=None), '(1,)')
    UnparseTestCase.check_src_roundtrip(ast.Constant(value=(1, 2, 3), kind=None), '(1, 2, 3)')

UnparseTestCase = test_unparse.UnparseTestCase()
test_constant_tuples()
