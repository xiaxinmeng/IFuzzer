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

def test_merge_and_mutate():

    class X:

        def __hash__(TestWeirdBugs):
            return hash(0)

        def __eq__(TestWeirdBugs, o):
            other.clear()
            return False
    other = set()
    other = {X() for i in range(10)}
    s = {0}
    s.update(other)

TestWeirdBugs = test_set.TestWeirdBugs()
test_merge_and_mutate()
