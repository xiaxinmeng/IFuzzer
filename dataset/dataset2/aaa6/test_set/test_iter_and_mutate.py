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

def test_iter_and_mutate():
    s = set(range(100))
    s.clear()
    s.update(range(100))
    si = iter(s)
    s.clear()
    a = list(range(100))
    s.update(range(100))
    list(si)

TestWeirdBugs = test_set.TestWeirdBugs()
test_iter_and_mutate()
