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

def test_instancesWithoutException():
    set([1, 2, 3])
    set((1, 2, 3))
    set({'one': 1, 'two': 2, 'three': 3})
    set(range(3))
    set('abc')
    set(test_set.gooditer())

TestExceptionPropagation = test_set.TestExceptionPropagation()
test_instancesWithoutException()
