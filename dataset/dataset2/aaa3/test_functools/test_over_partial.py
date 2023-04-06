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

def test_over_partial():
    TestPartialMethod.assertEqual(TestPartialMethod.a.over_partial(), ((TestPartialMethod.a, 7), {'c': 6}))
    TestPartialMethod.assertEqual(TestPartialMethod.a.over_partial(5), ((TestPartialMethod.a, 7, 5), {'c': 6}))
    TestPartialMethod.assertEqual(TestPartialMethod.a.over_partial(d=8), ((TestPartialMethod.a, 7), {'c': 6, 'd': 8}))
    TestPartialMethod.assertEqual(TestPartialMethod.a.over_partial(5, d=8), ((TestPartialMethod.a, 7, 5), {'c': 6, 'd': 8}))
    TestPartialMethod.assertEqual(TestPartialMethod.A.over_partial(TestPartialMethod.a, 5, d=8), ((TestPartialMethod.a, 7, 5), {'c': 6, 'd': 8}))

TestPartialMethod = test_functools.TestPartialMethod()
test_over_partial()
