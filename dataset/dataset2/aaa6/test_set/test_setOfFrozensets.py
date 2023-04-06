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

def test_setOfFrozensets():
    t = map(frozenset, ['abcdef', 'bcd', 'bdcb', 'fed', 'fedccba'])
    s = TestJointOps.thetype(t)
    TestJointOps.assertEqual(len(s), 3)

TestJointOps = test_set.TestJointOps()
test_setOfFrozensets()
