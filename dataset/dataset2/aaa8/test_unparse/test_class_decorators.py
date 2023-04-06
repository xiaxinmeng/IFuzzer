import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_class_decorators():
    UnparseTestCase.check_ast_roundtrip(test_unparse.class_decorator)

UnparseTestCase = test_unparse.UnparseTestCase()
test_class_decorators()
