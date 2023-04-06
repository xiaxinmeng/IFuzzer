import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_min_int():
    UnparseTestCase.check_ast_roundtrip(str(-2 ** 31))
    UnparseTestCase.check_ast_roundtrip(str(-2 ** 63))

UnparseTestCase = test_unparse.UnparseTestCase()
test_min_int()
