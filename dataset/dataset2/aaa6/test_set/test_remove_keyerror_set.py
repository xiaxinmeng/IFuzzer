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

def test_remove_keyerror_set():
    key = TestSet.thetype([3, 4])
    try:
        TestSet.s.remove(key)
    except KeyError as e:
        TestSet.assertTrue(e.args[0] is key, 'KeyError should be {0}, not {1}'.format(key, e.args[0]))
    else:
        TestSet.fail()

TestSet = test_set.TestSet()
TestSet.setUp()
test_remove_keyerror_set()
