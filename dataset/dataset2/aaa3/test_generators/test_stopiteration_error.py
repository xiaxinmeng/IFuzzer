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

def test_stopiteration_error():

    def gen():
        raise StopIteration
        yield
    with ExceptionTest.assertRaisesRegex(RuntimeError, 'raised StopIteration'):
        next(gen())

ExceptionTest = test_generators.ExceptionTest()
test_stopiteration_error()
