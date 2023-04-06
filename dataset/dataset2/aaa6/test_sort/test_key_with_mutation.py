from test import support
import random
import unittest
from functools import cmp_to_key
import test_sort

def test_key_with_mutation():
    data = list(range(10))

    def k(x):
        del data[:]
        data[:] = range(20)
        return x
    TestDecorateSortUndecorate.assertRaises(ValueError, data.sort, key=k)

TestDecorateSortUndecorate = test_sort.TestDecorateSortUndecorate()
test_key_with_mutation()
