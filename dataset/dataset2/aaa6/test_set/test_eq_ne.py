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

def test_eq_ne():
    TestOnlySetsInBinaryOps.assertEqual(TestOnlySetsInBinaryOps.other == TestOnlySetsInBinaryOps.set, False)
    TestOnlySetsInBinaryOps.assertEqual(TestOnlySetsInBinaryOps.set == TestOnlySetsInBinaryOps.other, False)
    TestOnlySetsInBinaryOps.assertEqual(TestOnlySetsInBinaryOps.other != TestOnlySetsInBinaryOps.set, True)
    TestOnlySetsInBinaryOps.assertEqual(TestOnlySetsInBinaryOps.set != TestOnlySetsInBinaryOps.other, True)

TestOnlySetsInBinaryOps = test_set.TestOnlySetsInBinaryOps()
test_eq_ne()
