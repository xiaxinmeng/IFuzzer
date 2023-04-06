import unittest
import sys
import pickle
import itertools
from test.support import ALWAYS_EQ
import test_range

def test_odd_bug():
    with RangeTest.assertRaises(TypeError):
        range([], 1, -1)

RangeTest = test_range.RangeTest()
test_odd_bug()
