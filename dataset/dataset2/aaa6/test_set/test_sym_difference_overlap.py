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

def test_sym_difference_overlap():
    TestBinaryOps.set ^= set((3, 4, 5))
    TestBinaryOps.assertEqual(TestBinaryOps.set, set([2, 3, 5, 6]))

TestBinaryOps = test_set.TestBinaryOps()
test_sym_difference_overlap()
