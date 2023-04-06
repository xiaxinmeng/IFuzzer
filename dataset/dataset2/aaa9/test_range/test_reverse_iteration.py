import unittest
import sys
import pickle
import itertools
from test.support import ALWAYS_EQ
import test_range

def test_reverse_iteration():
    for r in [range(10), range(0), range(1, 9, 3), range(8, 0, -3), range(sys.maxsize + 1, sys.maxsize + 10)]:
        RangeTest.assertEqual(list(reversed(r)), list(r)[::-1])

RangeTest = test_range.RangeTest()
test_reverse_iteration()
