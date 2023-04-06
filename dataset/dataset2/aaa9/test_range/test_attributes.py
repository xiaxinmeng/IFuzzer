import unittest
import sys
import pickle
import itertools
from test.support import ALWAYS_EQ
import test_range

def test_attributes():
    RangeTest.assert_attrs(range(0), 0, 0, 1)
    RangeTest.assert_attrs(range(10), 0, 10, 1)
    RangeTest.assert_attrs(range(-10), 0, -10, 1)
    RangeTest.assert_attrs(range(0, 10, 1), 0, 10, 1)
    RangeTest.assert_attrs(range(0, 10, 3), 0, 10, 3)
    RangeTest.assert_attrs(range(10, 0, -1), 10, 0, -1)
    RangeTest.assert_attrs(range(10, 0, -3), 10, 0, -3)
    RangeTest.assert_attrs(range(True), 0, 1, 1)
    RangeTest.assert_attrs(range(False, True), 0, 1, 1)
    RangeTest.assert_attrs(range(False, True, True), 0, 1, 1)

RangeTest = test_range.RangeTest()
test_attributes()
