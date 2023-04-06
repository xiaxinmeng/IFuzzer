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

def test_reuse_different_names():
    """Disallow this case because decorated function a would not be cached."""
    with TestCachedProperty.assertRaises(RuntimeError) as ctx:

        class ReusedCachedProperty:

            @test_functools.py_functools.cached_property
            def a(TestCachedProperty):
                pass
            b = a
    TestCachedProperty.assertEqual(str(ctx.exception.__context__), str(TypeError("Cannot assign the same cached_property to two different names ('a' and 'b').")))

TestCachedProperty = test_functools.TestCachedProperty()
test_reuse_different_names()
