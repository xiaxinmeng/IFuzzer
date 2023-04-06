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

def test_constructor_identity():
    s = TestSet.thetype(range(3))
    t = TestSet.thetype(s)
    TestSet.assertNotEqual(id(s), id(t))

TestSet = test_set.TestSet()
test_constructor_identity()
