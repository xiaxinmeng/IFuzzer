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

def test_lru_with_maxsize_none():

    @TestLRU.module.lru_cache(maxsize=None)
    def fib(n):
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)
    TestLRU.assertEqual([fib(n) for n in range(16)], [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610])
    TestLRU.assertEqual(fib.cache_info(), TestLRU.module._CacheInfo(hits=28, misses=16, maxsize=None, currsize=16))
    fib.cache_clear()
    TestLRU.assertEqual(fib.cache_info(), TestLRU.module._CacheInfo(hits=0, misses=0, maxsize=None, currsize=0))

TestLRU = test_functools.TestLRU()
test_lru_with_maxsize_none()
