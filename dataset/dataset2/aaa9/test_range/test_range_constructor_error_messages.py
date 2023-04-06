import unittest
import sys
import pickle
import itertools
from test.support import ALWAYS_EQ
import test_range

def test_range_constructor_error_messages():
    with RangeTest.assertRaisesRegex(TypeError, 'range expected at least 1 argument, got 0'):
        range()
    with RangeTest.assertRaisesRegex(TypeError, 'range expected at most 3 arguments, got 6'):
        range(1, 2, 3, 4, 5, 6)

RangeTest = test_range.RangeTest()
test_range_constructor_error_messages()
