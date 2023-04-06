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

def test_equality():
    TestJointOps.assertEqual(TestJointOps.s, set(TestJointOps.word))
    TestJointOps.assertEqual(TestJointOps.s, frozenset(TestJointOps.word))
    TestJointOps.assertEqual(TestJointOps.s == TestJointOps.word, False)
    TestJointOps.assertNotEqual(TestJointOps.s, set(TestJointOps.otherword))
    TestJointOps.assertNotEqual(TestJointOps.s, frozenset(TestJointOps.otherword))
    TestJointOps.assertEqual(TestJointOps.s != TestJointOps.word, True)

TestJointOps = test_set.TestJointOps()
test_equality()
