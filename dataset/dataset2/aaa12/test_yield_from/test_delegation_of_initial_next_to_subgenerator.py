import unittest
import inspect
from test.support import captured_stderr, disable_gc, gc_collect
from test import support
import test_yield_from

def test_delegation_of_initial_next_to_subgenerator():
    """
        Test delegation of initial next() call to subgenerator
        """
    trace = []

    def g1():
        trace.append('Starting g1')
        yield from g2()
        trace.append('Finishing g1')

    def g2():
        trace.append('Starting g2')
        yield 42
        trace.append('Finishing g2')
    for x in g1():
        trace.append('Yielded %s' % (x,))
    TestPEP380Operation.assertEqual(trace, ['Starting g1', 'Starting g2', 'Yielded 42', 'Finishing g2', 'Finishing g1'])

TestPEP380Operation = test_yield_from.TestPEP380Operation()
test_delegation_of_initial_next_to_subgenerator()
