import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_huge_float():
    UnparseTestCase.check_ast_roundtrip('1e1000')
    UnparseTestCase.check_ast_roundtrip('-1e1000')
    UnparseTestCase.check_ast_roundtrip('1e1000j')
    UnparseTestCase.check_ast_roundtrip('-1e1000j')

UnparseTestCase = test_unparse.UnparseTestCase()
test_huge_float()
