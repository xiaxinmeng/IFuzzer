import unittest
import inspect
from test.support import captured_stderr, disable_gc, gc_collect
from test import support
import test_yield_from

def test_custom_iterator_return():

    class MyIter:

        def __iter__(TestPEP380Operation):
            return TestPEP380Operation

        def __next__(TestPEP380Operation):
            raise StopIteration(42)

    def gen():
        nonlocal ret
        ret = (yield from MyIter())
    ret = None
    list(gen())
    TestPEP380Operation.assertEqual(ret, 42)

TestPEP380Operation = test_yield_from.TestPEP380Operation()
test_custom_iterator_return()
