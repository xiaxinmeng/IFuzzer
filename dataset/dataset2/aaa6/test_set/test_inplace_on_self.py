import unittest
from test import support
from test.support import warnings_helper
import gc
import weakref
import operator
import copy
import pickle
from random import randrange, shuffle
import warnings
import collections
import collections.abc
import itertools
from itertools import chain
import test_set

def test_inplace_on_TestSet():
    t = TestSet.s.copy()
    t |= t
    TestSet.assertEqual(t, TestSet.s)
    t &= t
    TestSet.assertEqual(t, TestSet.s)
    t -= t
    TestSet.assertEqual(t, TestSet.thetype())
    t = TestSet.s.copy()
    t ^= t
    TestSet.assertEqual(t, TestSet.thetype())

TestSet = test_set.TestSet()
TestSet.setUp()
test_inplace_on_TestSet()
