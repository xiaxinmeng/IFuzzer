import random
import unittest
import doctest
from test import support
from test.support import import_helper
from unittest import TestCase, skipUnless
from operator import itemgetter
from itertools import chain
import test_heapq

def test_empty_merges():
    TestHeap.assertEqual(list(TestHeap.module.merge([], [])), [])
    TestHeap.assertEqual(list(TestHeap.module.merge([], [], key=lambda : 6)), [])

TestHeap = test_heapq.TestHeap()
test_empty_merges()
