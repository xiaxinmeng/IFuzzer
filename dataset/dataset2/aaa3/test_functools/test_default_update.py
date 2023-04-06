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

def test_default_update():
    (wrapper, f) = TestUpdateWrapper._default_update()
    TestUpdateWrapper.check_wrapper(wrapper, f)
    TestUpdateWrapper.assertEqual(wrapper.__name__, 'f')
    TestUpdateWrapper.assertEqual(wrapper.__qualname__, f.__qualname__)
    TestUpdateWrapper.assertEqual(wrapper.attr, 'This is also a test')

TestUpdateWrapper = test_functools.TestUpdateWrapper()
test_default_update()
