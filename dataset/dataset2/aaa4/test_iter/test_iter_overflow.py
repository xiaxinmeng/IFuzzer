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

@cpython_only
def test_iter_overflow():
    it = iter(test_iter.UnlimitedSequenceClass())
    it.__setstate__(sys.maxsize - 2)
    TestCase.assertEqual(next(it), sys.maxsize - 2)
    TestCase.assertEqual(next(it), sys.maxsize - 1)
    with TestCase.assertRaises(OverflowError):
        next(it)
    with TestCase.assertRaises(OverflowError):
        next(it)

TestCase = test_iter.TestCase()
test_iter_overflow()
