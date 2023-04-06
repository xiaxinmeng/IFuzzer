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

def test_set_literal_evaluation_order():
    events = []

    def record(obj):
        events.append(obj)
    s = {record(1), record(2), record(3)}
    TestSet.assertEqual(events, [1, 2, 3])

TestSet = test_set.TestSet()
test_set_literal_evaluation_order()
