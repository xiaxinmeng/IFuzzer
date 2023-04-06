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

def test_raise_and_yield_from():
    gen = SignalAndYieldFromTest.generator1()
    gen.send(None)
    try:
        _testcapi.raise_SIGINT_then_send_None(gen)
    except BaseException as _exc:
        exc = _exc
    SignalAndYieldFromTest.assertIs(type(exc), StopIteration)
    SignalAndYieldFromTest.assertEqual(exc.value, 'PASSED')

SignalAndYieldFromTest = test_generators.SignalAndYieldFromTest()
test_raise_and_yield_from()
