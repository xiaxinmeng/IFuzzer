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

def test_update_operator():
    try:
        TestOnlySetsInBinaryOps.set |= TestOnlySetsInBinaryOps.other
    except TypeError:
        pass
    else:
        TestOnlySetsInBinaryOps.fail('expected TypeError')

TestOnlySetsInBinaryOps = test_set.TestOnlySetsInBinaryOps()
test_update_operator()
