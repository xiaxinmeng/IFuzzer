import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_annotations():
    UnparseTestCase.check_ast_roundtrip('def f(a : int): pass')
    UnparseTestCase.check_ast_roundtrip('def f(a: int = 5): pass')
    UnparseTestCase.check_ast_roundtrip('def f(*args: [int]): pass')
    UnparseTestCase.check_ast_roundtrip('def f(**kwargs: dict): pass')
    UnparseTestCase.check_ast_roundtrip('def f() -> None: pass')

UnparseTestCase = test_unparse.UnparseTestCase()
test_annotations()
