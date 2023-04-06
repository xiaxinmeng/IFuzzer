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

def test_container_iterator():

    class C(object):
        pass
    obj = C()
    ref = weakref.ref(obj)
    container = set([obj, 1])
    obj.x = iter(container)
    del obj, container
    gc.collect()
    TestJointOps.assertTrue(ref() is None, 'Cycle was not collected')

TestJointOps = test_set.TestJointOps()
TestJointOps.setUp()
test_container_iterator()
