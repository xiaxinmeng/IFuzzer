import unittest
import inspect
from test.support import captured_stderr, disable_gc, gc_collect
from test import support
import test_yield_from

def test_exception_value_crash():

    def g1():
        yield from g2()

    def g2():
        yield 'g2'
        return [42]
    TestPEP380Operation.assertEqual(list(g1()), ['g2'])

TestPEP380Operation = test_yield_from.TestPEP380Operation()
test_exception_value_crash()
