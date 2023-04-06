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

def test_with_bound_and_unbound_methods():
    data = list(map(str, range(10)))
    join = TestPartial.partial(str.join, '')
    TestPartial.assertEqual(join(data), '0123456789')
    join = TestPartial.partial(''.join)
    TestPartial.assertEqual(join(data), '0123456789')

TestPartial = test_functools.TestPartial()
test_with_bound_and_unbound_methods()
