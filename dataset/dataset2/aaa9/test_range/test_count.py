import unittest
import sys
import pickle
import itertools
from test.support import ALWAYS_EQ
import test_range

def test_count():
    RangeTest.assertEqual(range(3).count(-1), 0)
    RangeTest.assertEqual(range(3).count(0), 1)
    RangeTest.assertEqual(range(3).count(1), 1)
    RangeTest.assertEqual(range(3).count(2), 1)
    RangeTest.assertEqual(range(3).count(3), 0)
    RangeTest.assertIs(type(range(3).count(-1)), int)
    RangeTest.assertIs(type(range(3).count(1)), int)
    RangeTest.assertEqual(range(10 ** 20).count(1), 1)
    RangeTest.assertEqual(range(10 ** 20).count(10 ** 20), 0)
    RangeTest.assertEqual(range(3).index(1), 1)
    RangeTest.assertEqual(range(1, 2 ** 100, 2).count(2 ** 87), 0)
    RangeTest.assertEqual(range(1, 2 ** 100, 2).count(2 ** 87 + 1), 1)
    RangeTest.assertEqual(range(10).count(ALWAYS_EQ), 10)
    RangeTest.assertEqual(len(range(sys.maxsize, sys.maxsize + 10)), 10)

RangeTest = test_range.RangeTest()
test_count()
