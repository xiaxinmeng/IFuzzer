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

def test_pickle():

    def f():
        yield 1
    g = f()
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        with GeneratorTest.assertRaises((TypeError, pickle.PicklingError)):
            pickle.dumps(g, proto)

GeneratorTest = test_generators.GeneratorTest()
test_pickle()
