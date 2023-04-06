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

def test_error_iter():
    for typ in (test_iter.DefaultIterClass, test_iter.NoIterClass):
        TestCase.assertRaises(TypeError, iter, typ())
    TestCase.assertRaises(ZeroDivisionError, iter, test_iter.BadIterableClass())

TestCase = test_iter.TestCase()
test_error_iter()
