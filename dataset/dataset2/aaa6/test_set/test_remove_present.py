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

def test_remove_present():
    TestMutate.set.remove('b')
    TestMutate.assertEqual(TestMutate.set, set('ac'))

TestMutate = test_set.TestMutate()
TestMutate.setUp()
test_remove_present()
