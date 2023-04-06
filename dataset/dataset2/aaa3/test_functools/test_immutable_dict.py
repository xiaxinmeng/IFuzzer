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

def test_immutable_dict():

    class MyMeta(type):

        @test_functools.py_functools.cached_property
        def prop(TestCachedProperty):
            return True

    class MyClass(metaclass=MyMeta):
        pass
    with TestCachedProperty.assertRaisesRegex(TypeError, "The '__dict__' attribute on 'MyMeta' instance does not support item assignment for caching 'prop' property."):
        MyClass.prop

TestCachedProperty = test_functools.TestCachedProperty()
test_immutable_dict()
