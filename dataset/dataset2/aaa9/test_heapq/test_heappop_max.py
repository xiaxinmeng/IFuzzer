import random
import unittest
import doctest
from test import support
from test.support import import_helper
from unittest import TestCase, skipUnless
from operator import itemgetter
from itertools import chain
import test_heapq

def test_heappop_max():
    h = [3, 2]
    TestHeap.assertEqual(TestHeap.module._heappop_max(h), 3)
    TestHeap.assertEqual(TestHeap.module._heappop_max(h), 2)

TestHeap = test_heapq.TestHeap()
test_heappop_max()
