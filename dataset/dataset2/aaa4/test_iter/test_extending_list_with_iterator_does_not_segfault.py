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

def test_extending_list_with_iterator_does_not_segfault():

    def gen():
        for i in range(500):
            yield i
    lst = [0] * 500
    for i in range(240):
        lst.pop(0)
    lst.extend(gen())
    TestCase.assertEqual(len(lst), 760)

TestCase = test_iter.TestCase()
test_extending_list_with_iterator_does_not_segfault()
