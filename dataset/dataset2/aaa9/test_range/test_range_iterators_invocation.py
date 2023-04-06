import unittest
import sys
import pickle
import itertools
from test.support import ALWAYS_EQ
import test_range

def test_range_iterators_invocation():
    rangeiter_type = type(iter(range(0)))
    RangeTest.assertRaises(TypeError, rangeiter_type, 1, 3, 1)
    long_rangeiter_type = type(iter(range(1 << 1000)))
    RangeTest.assertRaises(TypeError, long_rangeiter_type, 1, 3, 1)

RangeTest = test_range.RangeTest()
test_range_iterators_invocation()
