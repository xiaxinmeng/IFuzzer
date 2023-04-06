import random
import unittest
import doctest
from test import support
from test.support import import_helper
from unittest import TestCase, skipUnless
from operator import itemgetter
from itertools import chain
import test_heapq

def test_heappush_mutating_heap():
    heap = []
    heap.extend((test_heapq.SideEffectLT(i, heap) for i in range(200)))
    with TestErrorHandling.assertRaises((IndexError, RuntimeError)):
        TestErrorHandling.module.heappush(heap, test_heapq.SideEffectLT(5, heap))

TestErrorHandling = test_heapq.TestErrorHandling()
test_heappush_mutating_heap()
