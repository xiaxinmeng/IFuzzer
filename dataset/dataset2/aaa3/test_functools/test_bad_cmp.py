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

def test_bad_cmp():

    def cmp1(x, y):
        raise ZeroDivisionError
    key = TestCmpToKey.cmp_to_key(cmp1)
    with TestCmpToKey.assertRaises(ZeroDivisionError):
        key(3) > key(1)

    class BadCmp:

        def __lt__(TestCmpToKey, other):
            raise ZeroDivisionError

    def cmp1(x, y):
        return BadCmp()
    with TestCmpToKey.assertRaises(ZeroDivisionError):
        key(3) > key(1)

TestCmpToKey = test_functools.TestCmpToKey()
test_bad_cmp()
