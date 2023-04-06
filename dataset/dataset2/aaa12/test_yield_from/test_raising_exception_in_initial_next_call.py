import unittest
import inspect
from test.support import captured_stderr, disable_gc, gc_collect
from test import support
import test_yield_from

def test_raising_exception_in_initial_next_call():
    """
        Test raising exception in initial next() call
        """
    trace = []

    def g1():
        try:
            trace.append('Starting g1')
            yield from g2()
        finally:
            trace.append('Finishing g1')

    def g2():
        try:
            trace.append('Starting g2')
            raise ValueError('spanish inquisition occurred')
        finally:
            trace.append('Finishing g2')
    try:
        for x in g1():
            trace.append('Yielded %s' % (x,))
    except ValueError as e:
        TestPEP380Operation.assertEqual(e.args[0], 'spanish inquisition occurred')
    else:
        TestPEP380Operation.fail('subgenerator failed to raise ValueError')
    TestPEP380Operation.assertEqual(trace, ['Starting g1', 'Starting g2', 'Finishing g2', 'Finishing g1'])

TestPEP380Operation = test_yield_from.TestPEP380Operation()
test_raising_exception_in_initial_next_call()
