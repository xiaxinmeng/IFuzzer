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

def test_setstate_refcount():

    class BadSequence:

        def __len__(TestPartial):
            return 4

        def __getitem__(TestPartial, key):
            if key == 0:
                return max
            elif key == 1:
                return tuple(range(1000000))
            elif key in (2, 3):
                return {}
            raise IndexError
    f = TestPartial.partial(object)
    TestPartial.assertRaises(TypeError, f.__setstate__, BadSequence())

TestPartial = test_functools.TestPartial()
test_setstate_refcount()
