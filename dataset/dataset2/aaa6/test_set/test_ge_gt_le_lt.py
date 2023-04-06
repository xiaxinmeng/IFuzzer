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

def test_ge_gt_le_lt():
    TestOnlySetsInBinaryOps.assertRaises(TypeError, lambda : TestOnlySetsInBinaryOps.set < TestOnlySetsInBinaryOps.other)
    TestOnlySetsInBinaryOps.assertRaises(TypeError, lambda : TestOnlySetsInBinaryOps.set <= TestOnlySetsInBinaryOps.other)
    TestOnlySetsInBinaryOps.assertRaises(TypeError, lambda : TestOnlySetsInBinaryOps.set > TestOnlySetsInBinaryOps.other)
    TestOnlySetsInBinaryOps.assertRaises(TypeError, lambda : TestOnlySetsInBinaryOps.set >= TestOnlySetsInBinaryOps.other)
    TestOnlySetsInBinaryOps.assertRaises(TypeError, lambda : TestOnlySetsInBinaryOps.other < TestOnlySetsInBinaryOps.set)
    TestOnlySetsInBinaryOps.assertRaises(TypeError, lambda : TestOnlySetsInBinaryOps.other <= TestOnlySetsInBinaryOps.set)
    TestOnlySetsInBinaryOps.assertRaises(TypeError, lambda : TestOnlySetsInBinaryOps.other > TestOnlySetsInBinaryOps.set)
    TestOnlySetsInBinaryOps.assertRaises(TypeError, lambda : TestOnlySetsInBinaryOps.other >= TestOnlySetsInBinaryOps.set)

TestOnlySetsInBinaryOps = test_set.TestOnlySetsInBinaryOps()
test_ge_gt_le_lt()
