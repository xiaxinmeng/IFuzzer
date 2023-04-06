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

def test_intersection_method_call():
    TestUpdateOps.set.intersection_update(set([3, 4, 5]))
    TestUpdateOps.assertEqual(TestUpdateOps.set, set([4]))

TestUpdateOps = test_set.TestUpdateOps()
TestUpdateOps.setUp()
test_intersection_method_call()
