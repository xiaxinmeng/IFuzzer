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

def test_throw_with_yield_from():

    def call_throw(gen):
        gen.throw(RuntimeError)
    GeneratorStackTraceTest.check_yield_from_example(call_throw)

GeneratorStackTraceTest = test_generators.GeneratorStackTraceTest()
test_throw_with_yield_from()
