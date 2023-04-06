import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_elifs():
    UnparseTestCase.check_ast_roundtrip(test_unparse.elif1)
    UnparseTestCase.check_ast_roundtrip(test_unparse.elif2)

UnparseTestCase = test_unparse.UnparseTestCase()
test_elifs()
