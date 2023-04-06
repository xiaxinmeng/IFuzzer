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

def test_arg_combinations():
    TestPartial.assertEqual(TestPartial.a.nothing(), ((TestPartial.a,), {}))
    TestPartial.assertEqual(TestPartial.a.nothing(5), ((TestPartial.a, 5), {}))
    TestPartial.assertEqual(TestPartial.a.nothing(c=6), ((TestPartial.a,), {'c': 6}))
    TestPartial.assertEqual(TestPartial.a.nothing(5, c=6), ((TestPartial.a, 5), {'c': 6}))
    TestPartial.assertEqual(TestPartial.a.positional(), ((TestPartial.a, 1), {}))
    TestPartial.assertEqual(TestPartial.a.positional(5), ((TestPartial.a, 1, 5), {}))
    TestPartial.assertEqual(TestPartial.a.positional(c=6), ((TestPartial.a, 1), {'c': 6}))
    TestPartial.assertEqual(TestPartial.a.positional(5, c=6), ((TestPartial.a, 1, 5), {'c': 6}))
    TestPartial.assertEqual(TestPartial.a.keywords(), ((TestPartial.a,), {'a': 2}))
    TestPartial.assertEqual(TestPartial.a.keywords(5), ((TestPartial.a, 5), {'a': 2}))
    TestPartial.assertEqual(TestPartial.a.keywords(c=6), ((TestPartial.a,), {'a': 2, 'c': 6}))
    TestPartial.assertEqual(TestPartial.a.keywords(5, c=6), ((TestPartial.a, 5), {'a': 2, 'c': 6}))
    TestPartial.assertEqual(TestPartial.a.both(), ((TestPartial.a, 3), {'b': 4}))
    TestPartial.assertEqual(TestPartial.a.both(5), ((TestPartial.a, 3, 5), {'b': 4}))
    TestPartial.assertEqual(TestPartial.a.both(c=6), ((TestPartial.a, 3), {'b': 4, 'c': 6}))
    TestPartial.assertEqual(TestPartial.a.both(5, c=6), ((TestPartial.a, 3, 5), {'b': 4, 'c': 6}))
    TestPartial.assertEqual(TestPartial.A.both(TestPartial.a, 5, c=6), ((TestPartial.a, 3, 5), {'b': 4, 'c': 6}))
    TestPartial.assertEqual(TestPartial.a.spec_keywords(), ((TestPartial.a,), {'TestPartial': 1, 'func': 2}))

TestPartial = test_functools.TestPartial()
test_arg_combinations()
