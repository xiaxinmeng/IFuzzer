import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_with_two_items():
    UnparseTestCase.check_ast_roundtrip(test_unparse.with_two_items)

UnparseTestCase = test_unparse.UnparseTestCase()
test_with_two_items()
