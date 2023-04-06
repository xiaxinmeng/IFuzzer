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

def test_badcmp():
    s = TestJointOps.thetype([BadCmp()])
    TestJointOps.assertRaises(RuntimeError, TestJointOps.thetype, [BadCmp(), BadCmp()])
    TestJointOps.assertRaises(RuntimeError, s.__contains__, BadCmp())
    if hasattr(s, 'add'):
        TestJointOps.assertRaises(RuntimeError, s.add, BadCmp())
        TestJointOps.assertRaises(RuntimeError, s.discard, BadCmp())
        TestJointOps.assertRaises(RuntimeError, s.remove, BadCmp())

TestJointOps = test_set.TestJointOps()
test_badcmp()
