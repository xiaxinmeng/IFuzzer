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

def test_invalid_positional_argument():

    @functools.singledispatch
    def f(*args):
        pass
    msg = 'f requires at least 1 positional argument'
    with TestSingleDispatch.assertRaisesRegex(TypeError, msg):
        f()

TestSingleDispatch = test_functools.TestSingleDispatch()
test_invalid_positional_argument()
