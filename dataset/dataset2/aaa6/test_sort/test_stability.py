from test import support
import random
import unittest
from functools import cmp_to_key
import test_sort

def test_stability():
    data = [(random.randrange(100), i) for i in range(200)]
    copy = data[:]
    data.sort(key=lambda t: t[0])
    copy.sort()
    TestDecorateSortUndecorate.assertEqual(data, copy)

TestDecorateSortUndecorate = test_sort.TestDecorateSortUndecorate()
test_stability()
