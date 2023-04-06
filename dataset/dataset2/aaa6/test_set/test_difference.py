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

def test_difference():
    TestJointOps.assertRaises(TypeError, lambda : TestJointOps.set - TestJointOps.other)
    TestJointOps.assertRaises(TypeError, lambda : TestJointOps.other - TestJointOps.set)
    if TestJointOps.otherIsIterable:
        TestJointOps.set.difference(TestJointOps.other)
    else:
        TestJointOps.assertRaises(TypeError, TestJointOps.set.difference, TestJointOps.other)

TestJointOps = test_set.TestJointOps()
test_difference()
