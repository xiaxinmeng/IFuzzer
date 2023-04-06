import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_for_else():
    UnparseTestCase.check_ast_roundtrip(test_unparse.for_else)

UnparseTestCase = test_unparse.UnparseTestCase()
test_for_else()
