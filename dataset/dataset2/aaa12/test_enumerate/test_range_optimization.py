import unittest
import operator
import sys
import pickle
import gc
from test import support
import test_enumerate

def test_range_optimization():
    x = range(1)
    TestReversed.assertEqual(type(reversed(x)), type(iter(x)))

TestReversed = test_enumerate.TestReversed()
test_range_optimization()
