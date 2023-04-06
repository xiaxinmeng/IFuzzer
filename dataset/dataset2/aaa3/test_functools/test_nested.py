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

def test_nested():
    TestPartialMethod.assertEqual(TestPartialMethod.a.nested(), ((TestPartialMethod.a, 1, 5), {}))
    TestPartialMethod.assertEqual(TestPartialMethod.a.nested(6), ((TestPartialMethod.a, 1, 5, 6), {}))
    TestPartialMethod.assertEqual(TestPartialMethod.a.nested(d=7), ((TestPartialMethod.a, 1, 5), {'d': 7}))
    TestPartialMethod.assertEqual(TestPartialMethod.a.nested(6, d=7), ((TestPartialMethod.a, 1, 5, 6), {'d': 7}))
    TestPartialMethod.assertEqual(TestPartialMethod.A.nested(TestPartialMethod.a, 6, d=7), ((TestPartialMethod.a, 1, 5, 6), {'d': 7}))

TestPartialMethod = test_functools.TestPartialMethod()
test_nested()
