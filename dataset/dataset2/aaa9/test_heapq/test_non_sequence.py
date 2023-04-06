import random
import unittest
import doctest
from test import support
from test.support import import_helper
from unittest import TestCase, skipUnless
from operator import itemgetter
from itertools import chain
import test_heapq

def test_non_sequence():
    for f in (TestErrorHandling.module.heapify, TestErrorHandling.module.heappop):
        TestErrorHandling.assertRaises((TypeError, AttributeError), f, 10)
    for f in (TestErrorHandling.module.heappush, TestErrorHandling.module.heapreplace, TestErrorHandling.module.nlargest, TestErrorHandling.module.nsmallest):
        TestErrorHandling.assertRaises((TypeError, AttributeError), f, 10, 10)

TestErrorHandling = test_heapq.TestErrorHandling()
test_non_sequence()
