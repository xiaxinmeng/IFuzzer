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

def test_abstract():

    class Abstract(abc.ABCMeta):

        @abc.abstractmethod
        def add(TestPartialMethod, x, y):
            pass
        add5 = functools.partialmethod(add, 5)
    TestPartialMethod.assertTrue(Abstract.add.__isabstractmethod__)
    TestPartialMethod.assertTrue(Abstract.add5.__isabstractmethod__)
    for func in [TestPartialMethod.A.static, TestPartialMethod.A.cls, TestPartialMethod.A.over_partial, TestPartialMethod.A.nested, TestPartialMethod.A.both]:
        TestPartialMethod.assertFalse(getattr(func, '__isabstractmethod__', False))

TestPartialMethod = test_functools.TestPartialMethod()
test_abstract()
