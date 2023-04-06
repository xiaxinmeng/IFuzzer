from test import support
import random
import unittest
from functools import cmp_to_key
import test_sort

def test_key_with_exception():
    data = list(range(-2, 2))
    dup = data[:]
    TestDecorateSortUndecorate.assertRaises(ZeroDivisionError, data.sort, key=lambda x: 1 / x)
    TestDecorateSortUndecorate.assertEqual(data, dup)

TestDecorateSortUndecorate = test_sort.TestDecorateSortUndecorate()
test_key_with_exception()
