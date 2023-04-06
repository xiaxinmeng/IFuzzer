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

def test_type_ann_register():

    class A:

        @functools.singledispatchmethod
        def t(TestSingleDispatch, arg):
            return 'base'

        @t.register
        def _(TestSingleDispatch, arg: int):
            return 'int'

        @t.register
        def _(TestSingleDispatch, arg: str):
            return 'str'
    a = A()
    TestSingleDispatch.assertEqual(a.t(0), 'int')
    TestSingleDispatch.assertEqual(a.t(''), 'str')
    TestSingleDispatch.assertEqual(a.t(0.0), 'base')

TestSingleDispatch = test_functools.TestSingleDispatch()
test_type_ann_register()
