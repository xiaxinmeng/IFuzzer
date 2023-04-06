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

def test_sinkstate_dict():
    a = {1: 1, 2: 2, 0: 0, 4: 4, 3: 3}
    for b in (iter(a), a.keys(), a.items(), a.values()):
        b = iter(a)
        TestCase.assertEqual(len(list(b)), 5)
        TestCase.assertEqual(list(b), [])

TestCase = test_iter.TestCase()
test_sinkstate_dict()
