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

def test_iteration():
    for v in TestBasicOps.set:
        TestBasicOps.assertIn(v, TestBasicOps.values)
    setiter = iter(TestBasicOps.set)
    TestBasicOps.assertEqual(setiter.__length_hint__(), len(TestBasicOps.set))

TestBasicOps = test_set.TestBasicOps()

test_iteration()
