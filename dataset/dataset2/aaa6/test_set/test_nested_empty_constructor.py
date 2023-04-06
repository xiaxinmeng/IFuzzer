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

def test_nested_empty_constructor():
    s = TestFrozenSetSubclass.thetype()
    t = TestFrozenSetSubclass.thetype(s)
    TestFrozenSetSubclass.assertEqual(s, t)

TestFrozenSetSubclass = test_set.TestFrozenSetSubclass()
test_nested_empty_constructor()
