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

def test_init():
    s = TestSet.thetype(TestSet.word)
    s.__init__(TestSet.otherword)
    TestSet.assertEqual(s, set(TestSet.word))

TestSet = test_set.TestSet()
TestSet.setUp()
test_init()
