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

def test_contains():
    for c in TestJointOps.letters:
        TestJointOps.assertEqual(c in TestJointOps.s, c in TestJointOps.d)
    TestJointOps.assertRaises(TypeError, TestJointOps.s.__contains__, [[]])
    s = TestJointOps.thetype([frozenset(TestJointOps.letters)])
    TestJointOps.assertIn(TestJointOps.thetype(TestJointOps.letters), s)

TestJointOps = test_set.TestJointOps()
test_contains()
