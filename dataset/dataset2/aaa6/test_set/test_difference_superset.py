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

def test_difference_superset():
    TestUpdateOps.set -= set((2, 4, 6, 8))
    TestUpdateOps.assertEqual(TestUpdateOps.set, set([]))

TestUpdateOps = test_set.TestUpdateOps()
TestUpdateOps.setUp()
test_difference_superset()
