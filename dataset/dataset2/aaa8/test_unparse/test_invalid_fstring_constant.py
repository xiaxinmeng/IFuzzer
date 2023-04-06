import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_invalid_fstring_constant():
    UnparseTestCase.check_invalid(ast.JoinedStr(values=[ast.Constant(value=100)]))

UnparseTestCase = test_unparse.UnparseTestCase()
test_invalid_fstring_constant()
