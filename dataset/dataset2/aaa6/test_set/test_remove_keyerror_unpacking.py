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

def test_remove_keyerror_unpacking():
    for v1 in ['Q', (1,)]:
        try:
            TestSet.s.remove(v1)
        except KeyError as e:
            v2 = e.args[0]
            TestSet.assertEqual(v1, v2)
        else:
            TestSet.fail()

TestSet = test_set.TestSet()
TestSet.setUp()
test_remove_keyerror_unpacking()
