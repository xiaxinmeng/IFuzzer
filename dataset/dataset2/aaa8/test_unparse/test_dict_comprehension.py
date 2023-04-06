import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_dict_comprehension():
    UnparseTestCase.check_ast_roundtrip('{x: x*x for x in range(10)}')

UnparseTestCase = test_unparse.UnparseTestCase()
test_dict_comprehension()
