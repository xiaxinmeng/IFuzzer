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

def test_pickling():
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        p = pickle.dumps(TestJointOps.set, proto)
        copy = pickle.loads(p)
        TestJointOps.assertEqual(TestJointOps.set, copy, '%s != %s' % (TestJointOps.set, copy))

TestJointOps = test_set.TestJointOps()
test_pickling()
