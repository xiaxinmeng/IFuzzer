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

def test_add():
    TestSet.s.add('Q')
    TestSet.assertIn('Q', TestSet.s)
    dup = TestSet.s.copy()
    TestSet.s.add('Q')
    TestSet.assertEqual(TestSet.s, dup)
    TestSet.assertRaises(TypeError, TestSet.s.add, [])

TestSet = test_set.TestSet()
TestSet.setUp()
test_add()
