import unittest
import inspect
from test.support import captured_stderr, disable_gc, gc_collect
from test import support
import test_yield_from

def test_yield_from_empty():

    def g():
        yield from ()
    TestPEP380Operation.assertRaises(StopIteration, next, g())

TestPEP380Operation = test_yield_from.TestPEP380Operation()
test_yield_from_empty()
