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

def test_empty_symmetric_difference():
    result = TestBasicOps.set ^ empty_set
    TestBasicOps.assertEqual(result, TestBasicOps.set)

TestBasicOps = test_set.TestBasicOps()
test_empty_symmetric_difference()
