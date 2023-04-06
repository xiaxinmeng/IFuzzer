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

def test_return_tuple():

    def g():
        return (yield 1)
    gen = g()
    ExceptionTest.assertEqual(next(gen), 1)
    with ExceptionTest.assertRaises(StopIteration) as cm:
        gen.send((2,))
    ExceptionTest.assertEqual(cm.exception.value, (2,))

ExceptionTest = test_generators.ExceptionTest()
test_return_tuple()
