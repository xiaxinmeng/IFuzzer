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

def test_total_ordering_no_overwrite():

    @functools.total_ordering
    class A(int):
        pass
    TestTotalOrdering.assertTrue(A(1) < A(2))
    TestTotalOrdering.assertTrue(A(2) > A(1))
    TestTotalOrdering.assertTrue(A(1) <= A(2))
    TestTotalOrdering.assertTrue(A(2) >= A(1))
    TestTotalOrdering.assertTrue(A(2) <= A(2))
    TestTotalOrdering.assertTrue(A(2) >= A(2))

TestTotalOrdering = test_functools.TestTotalOrdering()
test_total_ordering_no_overwrite()
