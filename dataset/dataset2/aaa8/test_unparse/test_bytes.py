import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_bytes():
    UnparseTestCase.check_ast_roundtrip("b'123'")

UnparseTestCase = test_unparse.UnparseTestCase()
test_bytes()
