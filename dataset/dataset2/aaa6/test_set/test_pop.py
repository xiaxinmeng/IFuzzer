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

def test_pop():
    popped = {}
    while TestSet.set:
        popped[TestSet.set.pop()] = None
    TestSet.assertEqual(len(popped), len(TestSet.values))
    for v in TestSet.values:
        TestSet.assertIn(v, popped)

TestSet = test_set.TestSet()
TestSet.setUp()
test_pop()
