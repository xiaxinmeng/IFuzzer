import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_invalid_set():
    UnparseTestCase.check_invalid(ast.Set(elts=[]))

UnparseTestCase = test_unparse.UnparseTestCase()
test_invalid_set()
