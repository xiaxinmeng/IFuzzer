import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_class_definition():
    UnparseTestCase.check_ast_roundtrip('class A(metaclass=type, *[], **{}): pass')

UnparseTestCase = test_unparse.UnparseTestCase()
test_class_definition()
