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

def test_gc():

    class A:
        pass
    s = set((A() for i in range(1000)))
    for elem in s:
        elem.cycle = s
        elem.sub = elem
        elem.set = set([elem])

TestJointOps = test_set.TestJointOps()
test_gc()
