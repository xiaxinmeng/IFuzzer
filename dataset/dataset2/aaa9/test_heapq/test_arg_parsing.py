import random
import unittest
import doctest
from test import support
from test.support import import_helper
from unittest import TestCase, skipUnless
from operator import itemgetter
from itertools import chain
import test_heapq

def test_arg_parsing():
    for f in (TestErrorHandling.module.heapify, TestErrorHandling.module.heappop, TestErrorHandling.module.heappush, TestErrorHandling.module.heapreplace, TestErrorHandling.module.nlargest, TestErrorHandling.module.nsmallest):
        TestErrorHandling.assertRaises((TypeError, AttributeError), f, 10)

TestErrorHandling = test_heapq.TestErrorHandling()
test_arg_parsing()
