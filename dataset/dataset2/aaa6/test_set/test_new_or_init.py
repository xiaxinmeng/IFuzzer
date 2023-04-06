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

def test_new_or_init():
    TestJointOps.assertRaises(TypeError, TestJointOps.thetype, [], 2)
    TestJointOps.assertRaises(TypeError, set().__init__, a=1)

TestJointOps = test_set.TestJointOps()
test_new_or_init()
