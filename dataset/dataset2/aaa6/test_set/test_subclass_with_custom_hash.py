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

def test_subclass_with_custom_hash():

    class H(TestJointOps.thetype):

        def __hash__(TestJointOps):
            return int(id(TestJointOps) & 2147483647)
    s = H()
    f = set()
    f.add(s)
    TestJointOps.assertIn(s, f)
    f.remove(s)
    f.add(s)
    f.discard(s)

TestJointOps = test_set.TestJointOps()
test_subclass_with_custom_hash()
