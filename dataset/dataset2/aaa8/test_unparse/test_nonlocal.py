import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_nonlocal():
    UnparseTestCase.check_ast_roundtrip(test_unparse.nonlocal_ex)

UnparseTestCase = test_unparse.UnparseTestCase()
test_nonlocal()
