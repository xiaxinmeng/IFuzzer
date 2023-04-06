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

def test_xor():
    i = TestJointOps.s.symmetric_difference(TestJointOps.otherword)
    TestJointOps.assertEqual(TestJointOps.s ^ set(TestJointOps.otherword), i)
    TestJointOps.assertEqual(TestJointOps.s ^ frozenset(TestJointOps.otherword), i)
    try:
        TestJointOps.s ^ TestJointOps.otherword
    except TypeError:
        pass
    else:
        TestJointOps.fail('s^t did not screen-out general iterables')

TestJointOps = test_set.TestJointOps()
test_xor()
