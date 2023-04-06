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

def test_sym_difference():
    TestOnlySetsInBinaryOps.assertRaises(TypeError, lambda : TestOnlySetsInBinaryOps.set ^ TestOnlySetsInBinaryOps.other)
    TestOnlySetsInBinaryOps.assertRaises(TypeError, lambda : TestOnlySetsInBinaryOps.other ^ TestOnlySetsInBinaryOps.set)
    if TestOnlySetsInBinaryOps.otherIsIterable:
        TestOnlySetsInBinaryOps.set.symmetric_difference(TestOnlySetsInBinaryOps.other)
    else:
        TestOnlySetsInBinaryOps.assertRaises(TypeError, TestOnlySetsInBinaryOps.set.symmetric_difference, TestOnlySetsInBinaryOps.other)

TestOnlySetsInBinaryOps = test_set.TestOnlySetsInBinaryOps()

test_sym_difference()
