import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_starred_assignment():
    UnparseTestCase.check_ast_roundtrip('a, *b, c = seq')
    UnparseTestCase.check_ast_roundtrip('a, (*b, c) = seq')
    UnparseTestCase.check_ast_roundtrip('a, *b[0], c = seq')
    UnparseTestCase.check_ast_roundtrip('a, *(b, c) = seq')

UnparseTestCase = test_unparse.UnparseTestCase()
test_starred_assignment()
