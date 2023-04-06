import unittest
from test.support import ALWAYS_EQ
import test_compare

def test_ne_high_priority():
    """object.__ne__() should allow reflected __ne__() to be tried"""
    calls = []

    class Left:

        def __eq__(*args):
            calls.append('Left.__eq__')
            return NotImplemented

    class Right:

        def __eq__(*args):
            calls.append('Right.__eq__')
            return NotImplemented

        def __ne__(*args):
            calls.append('Right.__ne__')
            return NotImplemented
    Left() != Right()
    ComparisonTest.assertSequenceEqual(calls, ['Left.__eq__', 'Right.__ne__'])

ComparisonTest = test_compare.ComparisonTest()
test_ne_high_priority()
