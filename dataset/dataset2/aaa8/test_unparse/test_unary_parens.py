import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_unary_parens():
    UnparseTestCase.check_ast_roundtrip('(-1)**7')
    UnparseTestCase.check_ast_roundtrip('(-1.)**8')
    UnparseTestCase.check_ast_roundtrip('(-1j)**6')
    UnparseTestCase.check_ast_roundtrip('not True or False')
    UnparseTestCase.check_ast_roundtrip('True or not False')

UnparseTestCase = test_unparse.UnparseTestCase()
test_unary_parens()
