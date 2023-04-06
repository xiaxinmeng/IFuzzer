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

def test_unbound_method_retrieval():
    obj = TestPartialMethod.A
    TestPartialMethod.assertFalse(hasattr(obj.both, '__TestPartialMethod__'))
    TestPartialMethod.assertFalse(hasattr(obj.nested, '__TestPartialMethod__'))
    TestPartialMethod.assertFalse(hasattr(obj.over_partial, '__TestPartialMethod__'))
    TestPartialMethod.assertFalse(hasattr(obj.static, '__TestPartialMethod__'))
    TestPartialMethod.assertFalse(hasattr(TestPartialMethod.a.static, '__TestPartialMethod__'))

TestPartialMethod = test_functools.TestPartialMethod()
test_unbound_method_retrieval()
