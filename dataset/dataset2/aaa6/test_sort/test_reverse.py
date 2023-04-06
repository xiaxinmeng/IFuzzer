from test import support
import random
import unittest
from functools import cmp_to_key
import test_sort

def test_reverse():
    data = list(range(100))
    random.shuffle(data)
    data.sort(reverse=True)
    TestDecorateSortUndecorate.assertEqual(data, list(range(99, -1, -1)))

TestDecorateSortUndecorate = test_sort.TestDecorateSortUndecorate()
test_reverse()
