import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_raise_from():
    UnparseTestCase.check_ast_roundtrip(test_unparse.raise_from)

UnparseTestCase = test_unparse.UnparseTestCase()
test_raise_from()
