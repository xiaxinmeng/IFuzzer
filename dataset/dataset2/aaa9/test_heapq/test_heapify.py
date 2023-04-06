import random
import unittest
import doctest
from test import support
from test.support import import_helper
from unittest import TestCase, skipUnless
from operator import itemgetter
from itertools import chain
import test_heapq

def test_heapify():
    for size in list(range(30)) + [20000]:
        heap = [random.random() for dummy in range(size)]
        TestHeap.module.heapify(heap)
        TestHeap.check_invariant(heap)
    TestHeap.assertRaises(TypeError, TestHeap.module.heapify, None)

TestHeap = test_heapq.TestHeap()
test_heapify()
