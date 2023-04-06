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

def test_intersection_non_overlap():
    TestBinaryOps.set &= set([8])
    TestBinaryOps.assertEqual(TestBinaryOps.set, test_set.empty_set)

TestBinaryOps = test_set.TestBinaryOps()
TestBinaryOps.setUp()
test_intersection_non_overlap()
