import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_try_except_finally():
    UnparseTestCase.check_ast_roundtrip(test_unparse.try_except_finally)

UnparseTestCase = test_unparse.UnparseTestCase()
test_try_except_finally()
