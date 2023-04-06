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

def test_set_literal_insertion_order():
    s = {1, 1.0, True}
    TestSet.assertEqual(len(s), 1)
    stored_value = s.pop()
    TestSet.assertEqual(type(stored_value), int)

TestSet = test_set.TestSet()
test_set_literal_insertion_order()
