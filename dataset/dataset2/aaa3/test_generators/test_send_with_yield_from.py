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

def test_send_with_yield_from():

    def call_send(gen):
        gen.send(None)
    GeneratorStackTraceTest.check_yield_from_example(call_send)

GeneratorStackTraceTest = test_generators.GeneratorStackTraceTest()
test_send_with_yield_from()
