import unittest
from test.support import ALWAYS_EQ
import test_compare

def test_ne_low_priority():
    """object.__ne__() should not invoke reflected __eq__()"""
    calls = []

    class Base:

        def __eq__(*args):
            calls.append('Base.__eq__')
            return NotImplemented

    class Derived(Base):

        def __eq__(*args):
            calls.append('Derived.__eq__')
            return NotImplemented

        def __ne__(*args):
            calls.append('Derived.__ne__')
            return NotImplemented
    Base() != Derived()
    ComparisonTest.assertSequenceEqual(calls, ['Derived.__ne__', 'Base.__eq__'])

ComparisonTest = test_compare.ComparisonTest()
test_ne_low_priority()
