import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_invalid_raise():
    UnparseTestCase.check_invalid(ast.Raise(exc=None, cause=ast.Name(id='X')))

UnparseTestCase = test_unparse.UnparseTestCase()
test_invalid_raise()
