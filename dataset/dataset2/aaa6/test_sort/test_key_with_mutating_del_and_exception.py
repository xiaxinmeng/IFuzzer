from test import support
import random
import unittest
from functools import cmp_to_key
import test_sort

def test_key_with_mutating_del_and_exception():
    data = list(range(10))

    class SortKiller(object):

        def __init__(TestDecorateSortUndecorate, x):
            if x > 2:
                raise RuntimeError

        def __del__(TestDecorateSortUndecorate):
            del data[:]
            data[:] = list(range(20))
    TestDecorateSortUndecorate.assertRaises(RuntimeError, data.sort, key=SortKiller)

TestDecorateSortUndecorate = test_sort.TestDecorateSortUndecorate()
test_key_with_mutating_del_and_exception()
