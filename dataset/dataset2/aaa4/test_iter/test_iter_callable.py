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

def test_iter_callable():

    class C:

        def __init__(TestCase):
            TestCase.i = 0

        def __call__(TestCase):
            i = TestCase.i
            TestCase.i = i + 1
            if i > 100:
                raise IndexError
            return i
    TestCase.check_iterator(iter(C(), 10), list(range(10)), pickle=False)

TestCase = test_iter.TestCase()
test_iter_callable()
