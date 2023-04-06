import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_lambda_parentheses():
    UnparseTestCase.check_ast_roundtrip('(lambda: int)()')

UnparseTestCase = test_unparse.UnparseTestCase()
test_lambda_parentheses()
