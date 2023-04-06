import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_function_arguments():
    UnparseTestCase.check_ast_roundtrip('def f(): pass')
    UnparseTestCase.check_ast_roundtrip('def f(a): pass')
    UnparseTestCase.check_ast_roundtrip('def f(b = 2): pass')
    UnparseTestCase.check_ast_roundtrip('def f(a, b): pass')
    UnparseTestCase.check_ast_roundtrip('def f(a, b = 2): pass')
    UnparseTestCase.check_ast_roundtrip('def f(a = 5, b = 2): pass')
    UnparseTestCase.check_ast_roundtrip('def f(*, a = 1, b = 2): pass')
    UnparseTestCase.check_ast_roundtrip('def f(*, a = 1, b): pass')
    UnparseTestCase.check_ast_roundtrip('def f(*, a, b = 2): pass')
    UnparseTestCase.check_ast_roundtrip('def f(a, b = None, *, c, **kwds): pass')
    UnparseTestCase.check_ast_roundtrip('def f(a=2, *args, c=5, d, **kwds): pass')
    UnparseTestCase.check_ast_roundtrip('def f(*args, **kwargs): pass')

UnparseTestCase = test_unparse.UnparseTestCase()
test_function_arguments()
