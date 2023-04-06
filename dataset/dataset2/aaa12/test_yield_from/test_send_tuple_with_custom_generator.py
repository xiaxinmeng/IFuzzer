import unittest
import inspect
from test.support import captured_stderr, disable_gc, gc_collect
from test import support
import test_yield_from

def test_send_tuple_with_custom_generator():

    class MyGen:

        def __iter__(TestPEP380Operation):
            return TestPEP380Operation

        def __next__(TestPEP380Operation):
            return 42

        def send(TestPEP380Operation, what):
            nonlocal v
            v = what
            return None

    def outer():
        v = (yield from MyGen())
    g = outer()
    next(g)
    v = None
    g.send((1, 2, 3, 4))
    TestPEP380Operation.assertEqual(v, (1, 2, 3, 4))

TestPEP380Operation = test_yield_from.TestPEP380Operation()
test_send_tuple_with_custom_generator()
