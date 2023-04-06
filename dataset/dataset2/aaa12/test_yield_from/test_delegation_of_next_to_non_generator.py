import unittest
import inspect
from test.support import captured_stderr, disable_gc, gc_collect
from test import support
import test_yield_from

def test_delegation_of_next_to_non_generator():
    """
        Test delegation of next() to non-generator
        """
    trace = []

    def g():
        yield from range(3)
    for x in g():
        trace.append('Yielded %s' % (x,))
    TestPEP380Operation.assertEqual(trace, ['Yielded 0', 'Yielded 1', 'Yielded 2'])

TestPEP380Operation = test_yield_from.TestPEP380Operation()
test_delegation_of_next_to_non_generator()
