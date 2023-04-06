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

def test_keystr_replaces_value():
    p = TestPartialC.partial(test_functools.capture)

    class MutatesYourDict(object):

        def __str__(TestPartialC):
            p.keywords[TestPartialC] = ['sth2']
            return 'astr'
    p.keywords[MutatesYourDict()] = ['sth']
    r = repr(p)
    TestPartialC.assertIn('astr', r)
    TestPartialC.assertIn("['sth']", r)

TestPartialC = test_functools.TestPartialC()
test_keystr_replaces_value()
