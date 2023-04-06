import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_strings():
    UnparseTestCase.check_ast_roundtrip("u'foo'")
    UnparseTestCase.check_ast_roundtrip("r'foo'")
    UnparseTestCase.check_ast_roundtrip("b'foo'")

UnparseTestCase = test_unparse.UnparseTestCase()
test_strings()
