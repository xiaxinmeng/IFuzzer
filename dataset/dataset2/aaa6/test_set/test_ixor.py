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

def test_ixor():
    TestSet.s ^= set(TestSet.otherword)
    for c in TestSet.word + TestSet.otherword:
        if (c in TestSet.word) ^ (c in TestSet.otherword):
            TestSet.assertIn(c, TestSet.s)
        else:
            TestSet.assertNotIn(c, TestSet.s)

TestSet = test_set.TestSet()
TestSet.setUp()
test_ixor()
