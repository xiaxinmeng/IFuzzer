import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_chained_comparisons():
    UnparseTestCase.check_ast_roundtrip('1 < 4 <= 5')
    UnparseTestCase.check_ast_roundtrip('a is b is c is not d')

UnparseTestCase = test_unparse.UnparseTestCase()
test_chained_comparisons()
