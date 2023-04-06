import unittest
import inspect
from test.support import captured_stderr, disable_gc, gc_collect
from test import support
import test_yield_from

def test_delegation_of_close_to_non_generator():
    """
        Test delegation of close() to non-generator
        """
    trace = []

    def g():
        try:
            trace.append('starting g')
            yield from range(3)
            trace.append('g should not be here')
        finally:
            trace.append('finishing g')
    gi = g()
    next(gi)
    with captured_stderr() as output:
        gi.close()
    TestPEP380Operation.assertEqual(output.getvalue(), '')
    TestPEP380Operation.assertEqual(trace, ['starting g', 'finishing g'])

TestPEP380Operation = test_yield_from.TestPEP380Operation()
test_delegation_of_close_to_non_generator()
