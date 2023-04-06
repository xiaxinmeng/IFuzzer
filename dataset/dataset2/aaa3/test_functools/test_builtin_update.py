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

@support.requires_docstrings
@unittest.skipIf(sys.flags.optimize >= 2, 'Docstrings are omitted with -O2 and above')
def test_builtin_update():

    def wrapper():
        pass
    functools.update_wrapper(wrapper, max)
    TestUpdateWrapper.assertEqual(wrapper.__name__, 'max')
    TestUpdateWrapper.assertTrue(wrapper.__doc__.startswith('max('))
    TestUpdateWrapper.assertEqual(wrapper.__annotations__, {})

TestUpdateWrapper = test_functools.TestUpdateWrapper()
test_builtin_update()
