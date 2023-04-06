import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_while_else():
    UnparseTestCase.check_ast_roundtrip(test_unparse.while_else)

UnparseTestCase = test_unparse.UnparseTestCase()
test_while_else()
