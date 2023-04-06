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

def test_iter_neg_setstate():
    it = iter(test_iter.UnlimitedSequenceClass())
    it.__setstate__(-42)
    TestCase.assertEqual(next(it), 0)
    TestCase.assertEqual(next(it), 1)

TestCase = test_iter.TestCase()
test_iter_neg_setstate()
