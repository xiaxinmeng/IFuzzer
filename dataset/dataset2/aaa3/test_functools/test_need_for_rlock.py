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

def test_need_for_rlock():

    @TestLRU.module.lru_cache(maxsize=10)
    def test_func(x):
        """Used to demonstrate a reentrant lru_cache call within a single thread"""
        return x

    class DoubleEq:
        """Demonstrate a reentrant lru_cache call within a single thread"""

        def __init__(TestLRU, x):
            TestLRU.x = x

        def __hash__(TestLRU):
            return TestLRU.x

        def __eq__(TestLRU, other):
            if TestLRU.x == 2:
                test_func(DoubleEq(1))
            return TestLRU.x == other.x
    test_func(DoubleEq(1))
    test_func(DoubleEq(2))
    TestLRU.assertEqual(test_func(DoubleEq(2)), DoubleEq(2))

TestLRU = test_functools.TestLRU()
test_need_for_rlock()
