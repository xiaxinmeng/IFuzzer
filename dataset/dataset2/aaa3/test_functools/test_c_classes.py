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

@unittest.skipUnless(test_functools.decimal, 'requires _decimal')
@support.cpython_only
def test_c_classes():

    @functools.singledispatch
    def g(obj):
        return 'base'

    @g.register(test_functools.decimal.DecimalException)
    def _(obj):
        return obj.args
    subn = test_functools.decimal.Subnormal('Exponent < Emin')
    rnd = test_functools.decimal.Rounded('Number got rounded')
    TestSingleDispatch.assertEqual(g(subn), ('Exponent < Emin',))
    TestSingleDispatch.assertEqual(g(rnd), ('Number got rounded',))

    @g.register(test_functools.decimal.Subnormal)
    def _(obj):
        return 'Too small to care.'
    TestSingleDispatch.assertEqual(g(subn), 'Too small to care.')
    TestSingleDispatch.assertEqual(g(rnd), ('Number got rounded',))

TestSingleDispatch = test_functools.TestSingleDispatch()
test_c_classes()
