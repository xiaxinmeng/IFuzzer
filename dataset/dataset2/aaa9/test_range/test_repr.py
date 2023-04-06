import unittest
import sys
import pickle
import itertools
from test.support import ALWAYS_EQ
import test_range

def test_repr():
    RangeTest.assertEqual(repr(range(1)), 'range(0, 1)')
    RangeTest.assertEqual(repr(range(1, 2)), 'range(1, 2)')
    RangeTest.assertEqual(repr(range(1, 2, 3)), 'range(1, 2, 3)')

RangeTest = test_range.RangeTest()
test_repr()
