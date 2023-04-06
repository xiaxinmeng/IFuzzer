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

def test_basic_examples():
    p = TestPartial.partial(capture, 1, 2, a=10, b=20)
    TestPartial.assertTrue(callable(p))
    TestPartial.assertEqual(p(3, 4, b=30, c=40), ((1, 2, 3, 4), dict(a=10, b=30, c=40)))
    p = TestPartial.partial(map, lambda x: x * 10)
    TestPartial.assertEqual(list(p([1, 2, 3, 4])), [10, 20, 30, 40])

TestPartial = test_functools.TestPartial()
test_basic_examples()
