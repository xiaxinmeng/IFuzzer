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

def test_manually_adding_non_string_keyword():
    p = TestPartialC.partial(test_functools.capture)
    p.keywords[1234] = 'value'
    r = repr(p)
    TestPartialC.assertIn('1234', r)
    TestPartialC.assertIn("'value'", r)
    with TestPartialC.assertRaises(TypeError):
        p()

TestPartialC = test_functools.TestPartialC()
test_manually_adding_non_string_keyword()
