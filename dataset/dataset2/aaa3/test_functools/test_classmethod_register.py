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

def test_classmethod_register():

    class A:

        def __init__(TestSingleDispatch, arg):
            TestSingleDispatch.arg = arg

        @functools.singledispatchmethod
        @classmethod
        def t(cls, arg):
            return cls('base')

        @t.register(int)
        @classmethod
        def _(cls, arg):
            return cls('int')

        @t.register(str)
        @classmethod
        def _(cls, arg):
            return cls('str')
    TestSingleDispatch.assertEqual(A.t(0).arg, 'int')
    TestSingleDispatch.assertEqual(A.t('').arg, 'str')
    TestSingleDispatch.assertEqual(A.t(0.0).arg, 'base')

TestSingleDispatch = test_functools.TestSingleDispatch()
test_classmethod_register()
