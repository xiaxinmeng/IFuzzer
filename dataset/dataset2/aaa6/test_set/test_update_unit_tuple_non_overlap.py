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

def test_update_unit_tuple_non_overlap():
    TestMutate.set.update(('a', 'z'))
    TestMutate.assertEqual(TestMutate.set, set(TestMutate.values + ['z']))

TestMutate = test_set.TestMutate()
TestMutate.setUp()
test_update_unit_tuple_non_overlap()
