import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_dict_unpacking_in_dict():
    UnparseTestCase.check_ast_roundtrip("{**{'y': 2}, 'x': 1}")
    UnparseTestCase.check_ast_roundtrip("{**{'y': 2}, **{'x': 1}}")

UnparseTestCase = test_unparse.UnparseTestCase()
test_dict_unpacking_in_dict()
