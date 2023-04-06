import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_set_literal():
    UnparseTestCase.check_ast_roundtrip("{'a', 'b', 'c'}")

UnparseTestCase = test_unparse.UnparseTestCase()
test_set_literal()
