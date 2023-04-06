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

def test_add_until_full():
    tmp = set()
    expected_len = 0
    for v in TestMutate.values:
        tmp.add(v)
        expected_len += 1
        TestMutate.assertEqual(len(tmp), expected_len)
    TestMutate.assertEqual(tmp, TestMutate.set)

TestMutate = test_set.TestMutate()
TestMutate.setUp()
test_add_until_full()
