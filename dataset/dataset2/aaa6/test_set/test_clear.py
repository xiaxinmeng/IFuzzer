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

def test_clear():
    TestSet.set.clear()
    TestSet.assertEqual(len(TestSet.set), 0)

TestSet = test_set.TestSet()
TestSet.setUp()
test_clear()
