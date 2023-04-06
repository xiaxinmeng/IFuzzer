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

def test_TestBasicOps_isdisjoint():
    result = TestBasicOps.set.isdisjoint(TestBasicOps.set)
    TestBasicOps.assertEqual(result, not TestBasicOps.set)

TestBasicOps = test_set.TestBasicOps()
test_TestBasicOps_isdisjoint()
