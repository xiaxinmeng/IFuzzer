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

def test_sinkstate_enumerate():
    a = range(5)
    e = enumerate(a)
    b = iter(e)
    TestCase.assertEqual(list(b), list(zip(range(5), range(5))))
    TestCase.assertEqual(list(b), [])

TestCase = test_iter.TestCase()
test_sinkstate_enumerate()
