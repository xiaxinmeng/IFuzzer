import unittest
import inspect
from test.support import captured_stderr, disable_gc, gc_collect
from test import support
import test_yield_from

def test_delegation_of_next_call_to_subgenerator():
    """
        Test delegation of next() call to subgenerator
        """
    trace = []

    def g1():
        trace.append('Starting g1')
        yield 'g1 ham'
        yield from g2()
        yield 'g1 eggs'
        trace.append('Finishing g1')

    def g2():
        trace.append('Starting g2')
        yield 'g2 spam'
        yield 'g2 more spam'
        trace.append('Finishing g2')
    for x in g1():
        trace.append('Yielded %s' % (x,))
    TestPEP380Operation.assertEqual(trace, ['Starting g1', 'Yielded g1 ham', 'Starting g2', 'Yielded g2 spam', 'Yielded g2 more spam', 'Finishing g2', 'Yielded g1 eggs', 'Finishing g1'])

TestPEP380Operation = test_yield_from.TestPEP380Operation()
test_delegation_of_next_call_to_subgenerator()
