import sys
import unittest
from test.support import run_unittest, cpython_only
from test.support.os_helper import TESTFN, unlink
from test.support import check_free_after_iterating, ALWAYS_EQ, NEVER_EQ
import pickle
import collections.abc
from operator import countOf
from operator import indexOf
import test_iter

def test_sinkstate_tuple():
    a = (0, 1, 2, 3, 4)
    b = iter(a)
    TestCase.assertEqual(list(b), list(range(5)))
    TestCase.assertEqual(list(b), [])

TestCase = test_iter.TestCase()
test_sinkstate_tuple()
