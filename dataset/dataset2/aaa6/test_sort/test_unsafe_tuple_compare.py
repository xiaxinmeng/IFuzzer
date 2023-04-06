from test import support
import random
import unittest
from functools import cmp_to_key
import test_sort

def test_unsafe_tuple_compare():
    test_sort.check_against_PyObject_RichCompareBool(TestOptimizedCompares, [float('nan')] * 100)
    test_sort.check_against_PyObject_RichCompareBool(TestOptimizedCompares, [float('nan') for _ in range(100)])

TestOptimizedCompares = test_sort.TestOptimizedCompares()
test_unsafe_tuple_compare()
