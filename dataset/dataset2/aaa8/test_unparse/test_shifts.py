import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_shifts():
    UnparseTestCase.check_ast_roundtrip('45 << 2')
    UnparseTestCase.check_ast_roundtrip('13 >> 7')

UnparseTestCase = test_unparse.UnparseTestCase()
test_shifts()
