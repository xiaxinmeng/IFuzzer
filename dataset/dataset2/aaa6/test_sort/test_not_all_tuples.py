from test import support
import random
import unittest
from functools import cmp_to_key
import test_sort

def test_not_all_tuples():
    TestOptimizedCompares.assertRaises(TypeError, [(1.0, 1.0), (False, 'A'), 6].sort)
    TestOptimizedCompares.assertRaises(TypeError, [('a', 1), (1, 'a')].sort)
    TestOptimizedCompares.assertRaises(TypeError, [(1, 'a'), ('a', 1)].sort)

TestOptimizedCompares = test_sort.TestOptimizedCompares()
test_not_all_tuples()
