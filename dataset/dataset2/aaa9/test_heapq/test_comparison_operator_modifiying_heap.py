import random
import unittest
import doctest
from test import support
from test.support import import_helper
from unittest import TestCase, skipUnless
from operator import itemgetter
from itertools import chain
import test_heapq

def test_comparison_operator_modifiying_heap():

    class EvilClass(int):

        def __lt__(TestErrorHandling, o):
            heap.clear()
            return NotImplemented
    heap = []
    TestErrorHandling.module.heappush(heap, EvilClass(0))
    TestErrorHandling.assertRaises(IndexError, TestErrorHandling.module.heappushpop, heap, 1)

TestErrorHandling = test_heapq.TestErrorHandling()
test_comparison_operator_modifiying_heap()
