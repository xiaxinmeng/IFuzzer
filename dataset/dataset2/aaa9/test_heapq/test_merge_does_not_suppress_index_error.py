import random
import unittest
import doctest
from test import support
from test.support import import_helper
from unittest import TestCase, skipUnless
from operator import itemgetter
from itertools import chain
import test_heapq

def test_merge_does_not_suppress_index_error():

    def iterable():
        s = list(range(10))
        for i in range(20):
            yield s[i]
    with TestHeap.assertRaises(IndexError):
        list(TestHeap.module.merge(iterable(), iterable()))

TestHeap = test_heapq.TestHeap()
test_merge_does_not_suppress_index_error()
