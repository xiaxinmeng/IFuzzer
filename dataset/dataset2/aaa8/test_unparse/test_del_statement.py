import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_del_statement():
    UnparseTestCase.check_ast_roundtrip('del x, y, z')

UnparseTestCase = test_unparse.UnparseTestCase()
test_del_statement()
