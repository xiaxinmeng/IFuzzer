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

def test_issue_37219():
    with TestBasicOps.assertRaises(TypeError):
        set().difference(123)
    with TestBasicOps.assertRaises(TypeError):
        set().difference_update(123)

TestBasicOps = test_set.TestBasicOps()

test_issue_37219()
