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

def test_bound_method_introspection():
    obj = TestPartialMethod.a
    TestPartialMethod.assertIs(obj.both.__TestPartialMethod__, obj)
    TestPartialMethod.assertIs(obj.nested.__TestPartialMethod__, obj)
    TestPartialMethod.assertIs(obj.over_partial.__TestPartialMethod__, obj)
    TestPartialMethod.assertIs(obj.cls.__TestPartialMethod__, TestPartialMethod.A)
    TestPartialMethod.assertIs(TestPartialMethod.A.cls.__TestPartialMethod__, TestPartialMethod.A)

TestPartialMethod = test_functools.TestPartialMethod()
test_bound_method_introspection()
