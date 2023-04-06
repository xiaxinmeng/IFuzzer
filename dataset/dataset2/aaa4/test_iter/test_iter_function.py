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

def test_iter_function():

    def spam(state=[0]):
        i = state[0]
        state[0] = i + 1
        return i
    TestCase.check_iterator(iter(spam, 10), list(range(10)), pickle=False)

TestCase = test_iter.TestCase()
test_iter_function()
