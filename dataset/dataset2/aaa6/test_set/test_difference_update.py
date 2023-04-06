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

def test_difference_update():
    if TestSet.otherIsIterable:
        TestSet.set.difference_update(TestSet.other)
    else:
        TestSet.assertRaises(TypeError, TestSet.set.difference_update, TestSet.other)

TestSet = test_set.TestSet()
TestSet.setUp()
test_difference_update()
