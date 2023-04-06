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

def test_3720():

    class BadIterator(object):

        def __iter__(TestCase):
            return TestCase

        def __next__(TestCase):
            del BadIterator.__next__
            return 1
    try:
        for i in BadIterator():
            pass
    except TypeError:
        pass

TestCase = test_iter.TestCase()
test_3720()
