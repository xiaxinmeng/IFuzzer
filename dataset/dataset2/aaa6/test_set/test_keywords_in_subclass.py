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

def test_keywords_in_subclass():
    """SF bug #1486663 -- this used to erroneously raise a TypeError"""
    test_set.SetSubclassWithKeywordArgs(newarg=1)

TestSetSubclassWithKeywordArgs = test_set.TestSetSubclassWithKeywordArgs()
test_keywords_in_subclass()
