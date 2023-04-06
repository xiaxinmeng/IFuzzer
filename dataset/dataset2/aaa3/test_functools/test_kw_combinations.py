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

def test_kw_combinations():
    p = TestPartial.partial(capture)
    TestPartial.assertEqual(p.keywords, {})
    TestPartial.assertEqual(p(), ((), {}))
    TestPartial.assertEqual(p(a=1), ((), {'a': 1}))
    p = TestPartial.partial(capture, a=1)
    TestPartial.assertEqual(p.keywords, {'a': 1})
    TestPartial.assertEqual(p(), ((), {'a': 1}))
    TestPartial.assertEqual(p(b=2), ((), {'a': 1, 'b': 2}))
    TestPartial.assertEqual(p(a=3, b=2), ((), {'a': 3, 'b': 2}))

TestPartial = test_functools.TestPartial()
test_kw_combinations()
