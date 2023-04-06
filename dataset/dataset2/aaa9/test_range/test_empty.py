import unittest
import sys
import pickle
import itertools
from test.support import ALWAYS_EQ
import test_range

def test_empty():
    r = range(0)
    RangeTest.assertNotIn(0, r)
    RangeTest.assertNotIn(1, r)
    r = range(0, -10)
    RangeTest.assertNotIn(0, r)
    RangeTest.assertNotIn(-1, r)
    RangeTest.assertNotIn(1, r)

RangeTest = test_range.RangeTest()
test_empty()
