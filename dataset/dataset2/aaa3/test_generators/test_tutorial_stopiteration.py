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

def test_tutorial_stopiteration():

    def f():
        yield 1
        raise StopIteration
        yield 2
    g = f()
    ExceptionTest.assertEqual(next(g), 1)
    with ExceptionTest.assertRaisesRegex(RuntimeError, 'raised StopIteration'):
        next(g)

ExceptionTest = test_generators.ExceptionTest()
test_tutorial_stopiteration()
