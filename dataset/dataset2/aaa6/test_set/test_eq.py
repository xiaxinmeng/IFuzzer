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

def test_eq():
    TestBinaryOps.assertEqual(TestBinaryOps.set, set({2: 1, 4: 3, 6: 5}))

TestBinaryOps = test_set.TestBinaryOps()
TestBinaryOps.setUp()
test_eq()
