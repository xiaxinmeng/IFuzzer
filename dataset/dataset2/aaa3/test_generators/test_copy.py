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

def test_copy():

    def f():
        yield 1
    g = f()
    with GeneratorTest.assertRaises(TypeError):
        copy.copy(g)

GeneratorTest = test_generators.GeneratorTest()
test_copy()
