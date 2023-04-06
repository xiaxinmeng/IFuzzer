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

@unittest.skipUnless(hasattr(set, 'test_c_api'), 'C API test only available in a debug build')
def test_c_api():
    TestSet.assertEqual(set().test_c_api(), True)

TestSet = test_set.TestSet()
test_c_api()
