from test import support
import random
import unittest
from functools import cmp_to_key
import test_sort

def test_key_with_mutating_del():
    data = list(range(10))

    class SortKiller(object):

        def __init__(TestDecorateSortUndecorate, x):
            pass

        def __del__(TestDecorateSortUndecorate):
            del data[:]
            data[:] = range(20)

        def __lt__(TestDecorateSortUndecorate, other):
            return id(TestDecorateSortUndecorate) < id(other)
    TestDecorateSortUndecorate.assertRaises(ValueError, data.sort, key=SortKiller)

TestDecorateSortUndecorate = test_sort.TestDecorateSortUndecorate()
test_key_with_mutating_del()
