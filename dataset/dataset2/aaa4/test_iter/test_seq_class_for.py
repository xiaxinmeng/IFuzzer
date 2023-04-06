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

def test_seq_class_for():
    TestCase.check_for_loop(test_iter.SequenceClass(10), list(range(10)))

TestCase = test_iter.TestCase()
test_seq_class_for()
