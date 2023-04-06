import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_imaginary_literals():
    UnparseTestCase.check_ast_roundtrip('7j')
    UnparseTestCase.check_ast_roundtrip('-7j')
    UnparseTestCase.check_ast_roundtrip('0j')
    UnparseTestCase.check_ast_roundtrip('-0j')

UnparseTestCase = test_unparse.UnparseTestCase()
test_imaginary_literals()
