import unittest
import inspect
from test.support import captured_stderr, disable_gc, gc_collect
from test import support
import test_yield_from

def test_value_attribute_of_StopIteration_exception():
    """
        Test 'value' attribute of StopIteration exception
        """
    trace = []

    def pex(e):
        trace.append('%s: %s' % (e.__class__.__name__, e))
        trace.append('value = %s' % (e.value,))
    e = StopIteration()
    pex(e)
    e = StopIteration('spam')
    pex(e)
    e.value = 'eggs'
    pex(e)
    TestPEP380Operation.assertEqual(trace, ['StopIteration: ', 'value = None', 'StopIteration: spam', 'value = spam', 'StopIteration: spam', 'value = eggs'])

TestPEP380Operation = test_yield_from.TestPEP380Operation()
test_value_attribute_of_StopIteration_exception()
