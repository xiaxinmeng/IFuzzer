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

def test_stop_sequence():

    class MySequenceClass(test_iter.SequenceClass):

        def __getitem__(TestCase, i):
            if i == 10:
                raise StopIteration
            return test_iter.SequenceClass.__getitem__(TestCase, i)
    TestCase.check_for_loop(MySequenceClass(20), list(range(10)), pickle=False)

TestCase = test_iter.TestCase()
test_stop_sequence()
