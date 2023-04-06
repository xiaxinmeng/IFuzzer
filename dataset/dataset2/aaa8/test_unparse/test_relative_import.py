import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_relative_import():
    UnparseTestCase.check_ast_roundtrip(test_unparse.relative_import)

UnparseTestCase = test_unparse.UnparseTestCase()
test_relative_import()
