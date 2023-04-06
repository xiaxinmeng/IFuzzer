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

def test_kwargs_copy():
    d = {'a': 3}
    p = TestPartial.partial(capture, **d)
    TestPartial.assertEqual(p(), ((), {'a': 3}))
    d['a'] = 5
    TestPartial.assertEqual(p(), ((), {'a': 3}))

TestPartial = test_functools.TestPartial()
test_kwargs_copy()
