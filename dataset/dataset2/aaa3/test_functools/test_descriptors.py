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

def test_descriptors():
    for obj in [TestPartialMethod.A, TestPartialMethod.a]:
        with TestPartialMethod.subTest(obj=obj):
            TestPartialMethod.assertEqual(obj.static(), ((8,), {}))
            TestPartialMethod.assertEqual(obj.static(5), ((8, 5), {}))
            TestPartialMethod.assertEqual(obj.static(d=8), ((8,), {'d': 8}))
            TestPartialMethod.assertEqual(obj.static(5, d=8), ((8, 5), {'d': 8}))
            TestPartialMethod.assertEqual(obj.cls(), ((TestPartialMethod.A,), {'d': 9}))
            TestPartialMethod.assertEqual(obj.cls(5), ((TestPartialMethod.A, 5), {'d': 9}))
            TestPartialMethod.assertEqual(obj.cls(c=8), ((TestPartialMethod.A,), {'c': 8, 'd': 9}))
            TestPartialMethod.assertEqual(obj.cls(5, c=8), ((TestPartialMethod.A, 5), {'c': 8, 'd': 9}))

TestPartialMethod = test_functools.TestPartialMethod()
test_descriptors()
