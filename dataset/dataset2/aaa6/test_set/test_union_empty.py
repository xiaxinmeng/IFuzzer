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

def test_union_empty():
    result = test_set.empty_set | TestBasicOps.set
    TestBasicOps.assertEqual(result, TestBasicOps.dup)

TestBasicOps = test_set.TestBasicOps()
test_union_empty()
