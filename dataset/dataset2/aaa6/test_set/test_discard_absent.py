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

def test_discard_absent():
    TestMutate.set.discard('d')
    TestMutate.assertEqual(TestMutate.set, set('abc'))

TestMutate = test_set.TestMutate()
TestMutate.setUp()
test_discard_absent()
