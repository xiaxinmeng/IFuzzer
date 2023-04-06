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

def test_discard():
    TestSet.s.discard('a')
    TestSet.assertNotIn('a', TestSet.s)
    TestSet.s.discard('Q')
    TestSet.assertRaises(TypeError, TestSet.s.discard, [])
    s = TestSet.thetype([frozenset(TestSet.word)])
    TestSet.assertIn(TestSet.thetype(TestSet.word), s)
    s.discard(TestSet.thetype(TestSet.word))
    TestSet.assertNotIn(TestSet.thetype(TestSet.word), s)
    s.discard(TestSet.thetype(TestSet.word))

TestSet = test_set.TestSet()
TestSet.setUp()
test_discard()
