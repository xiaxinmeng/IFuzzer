import unittest
import inspect
from test.support import captured_stderr, disable_gc, gc_collect
from test import support
import test_yield_from

def test_conversion_of_sendNone_to_next():
    """
        Test conversion of send(None) to next()
        """
    trace = []

    def g():
        yield from range(3)
    gi = g()
    for x in range(3):
        y = gi.send(None)
        trace.append('Yielded: %s' % (y,))
    TestPEP380Operation.assertEqual(trace, ['Yielded: 0', 'Yielded: 1', 'Yielded: 2'])

TestPEP380Operation = test_yield_from.TestPEP380Operation()
test_conversion_of_sendNone_to_next()
