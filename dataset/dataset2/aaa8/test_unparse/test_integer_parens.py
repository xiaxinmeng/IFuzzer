import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_integer_parens():
    UnparseTestCase.check_ast_roundtrip('3 .__abs__()')

UnparseTestCase = test_unparse.UnparseTestCase()
test_integer_parens()
