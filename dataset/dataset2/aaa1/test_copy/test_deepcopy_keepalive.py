import copy
import copyreg
import weakref
import abc
from operator import le, lt, ge, gt, eq, ne
import unittest
import test_copy

def test_deepcopy_keepalive():
    memo = {}
    x = []
    y = copy.deepcopy(x, memo)
    TestCopy.assertIs(memo[id(memo)][0], x)

TestCopy = test_copy.TestCopy()
test_deepcopy_keepalive()
