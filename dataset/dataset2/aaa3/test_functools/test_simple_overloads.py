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

def test_simple_overloads():

    @functools.singledispatch
    def g(obj):
        return 'base'

    def g_int(i):
        return 'integer'
    g.register(int, g_int)
    TestSingleDispatch.assertEqual(g('str'), 'base')
    TestSingleDispatch.assertEqual(g(1), 'integer')
    TestSingleDispatch.assertEqual(g([1, 2, 3]), 'base')

TestSingleDispatch = test_functools.TestSingleDispatch()
test_simple_overloads()
