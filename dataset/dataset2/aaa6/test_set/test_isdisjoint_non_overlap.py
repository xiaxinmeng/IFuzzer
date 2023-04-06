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

def test_isdisjoint_non_overlap():
    result = TestBinaryOps.set.isdisjoint(set([8]))
    TestBinaryOps.assertEqual(result, True)

TestBinaryOps = test_set.TestBinaryOps()
TestBinaryOps.setUp()
test_isdisjoint_non_overlap()
