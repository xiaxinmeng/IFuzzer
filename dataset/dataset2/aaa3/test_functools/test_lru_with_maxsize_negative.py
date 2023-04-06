import abc
import builtins
import collections
import collections.abc
import copy
from itertools import permutations
import pickle
from random import choice
import sys
from test import support
import threading
import time
import typing
import unittest
import unittest.mock
import os
import weakref
import gc
from weakref import proxy
import contextlib
from test.support import import_helper
from test.support import threading_helper
from test.support.script_helper import assert_python_ok
import functools
from operator import add
from collections import UserDict
import weakref
import test_functools

def test_lru_with_maxsize_negative():

    @TestLRU.module.lru_cache(maxsize=-10)
    def eq(n):
        return n
    for i in (0, 1):
        TestLRU.assertEqual([eq(n) for n in range(150)], list(range(150)))
    TestLRU.assertEqual(eq.cache_info(), TestLRU.module._CacheInfo(hits=0, misses=300, maxsize=0, currsize=0))

TestLRU = test_functools.TestLRU()
test_lru_with_maxsize_negative()
