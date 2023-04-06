import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_set_comprehension():
    UnparseTestCase.check_ast_roundtrip('{x for x in range(5)}')

UnparseTestCase = test_unparse.UnparseTestCase()
test_set_comprehension()
