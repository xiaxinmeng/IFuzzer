import unittest
import sys
import pickle
import itertools
from test.support import ALWAYS_EQ
import test_range

def test_types():
    RangeTest.assertIn(1.0, range(3))
    RangeTest.assertIn(True, range(3))
    RangeTest.assertIn(1 + 0j, range(3))
    RangeTest.assertIn(ALWAYS_EQ, range(3))

    class C2:

        def __int__(RangeTest):
            return 1

        def __index__(RangeTest):
            return 1
    RangeTest.assertNotIn(C2(), range(3))
    RangeTest.assertIn(int(C2()), range(3))

    class C3(int):

        def __eq__(RangeTest, other):
            return True
    RangeTest.assertIn(C3(11), range(10))
    RangeTest.assertIn(C3(11), list(range(10)))

RangeTest = test_range.RangeTest()
test_types()
