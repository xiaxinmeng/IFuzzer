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

def test_isdisjoint_overlap():
    result = TestBinaryOps.set.isdisjoint(set([3, 4, 5]))
    TestBinaryOps.assertEqual(result, False)

TestBinaryOps = test_set.TestBinaryOps()
TestBinaryOps.setUp()
test_isdisjoint_overlap()
