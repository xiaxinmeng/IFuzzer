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

def test_kwargs_order():

    @TestLRU.module.lru_cache(maxsize=10)
    def f(**kwargs):
        return list(kwargs.items())
    TestLRU.assertEqual(f(a=1, b=2), [('a', 1), ('b', 2)])
    TestLRU.assertEqual(f(b=2, a=1), [('b', 2), ('a', 1)])
    TestLRU.assertEqual(f.cache_info(), TestLRU.module._CacheInfo(hits=0, misses=2, maxsize=10, currsize=2))

TestLRU = test_functools.TestLRU()
test_kwargs_order()
