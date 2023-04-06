import copy
import gc
import pickle
import sys
import unittest
import weakref
import inspect
from test import support
import _testcapi
from test import support, test_generators
import test_generators

def test_except_next():

    def gen():
        ExceptionTest.assertEqual(sys.exc_info()[0], ValueError)
        yield 'done'
    g = gen()
    try:
        raise ValueError
    except Exception:
        ExceptionTest.assertEqual(next(g), 'done')
    ExceptionTest.assertEqual(sys.exc_info(), (None, None, None))

ExceptionTest = test_generators.ExceptionTest()
test_except_next()
