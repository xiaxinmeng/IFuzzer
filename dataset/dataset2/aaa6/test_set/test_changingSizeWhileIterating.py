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

def test_changingSizeWhileIterating():
    s = set([1, 2, 3])
    try:
        for i in s:
            s.update([4])
    except RuntimeError:
        pass
    else:
        TestExceptionPropagation.fail('no exception when changing size during iteration')

TestExceptionPropagation = test_set.TestExceptionPropagation()
test_changingSizeWhileIterating()
