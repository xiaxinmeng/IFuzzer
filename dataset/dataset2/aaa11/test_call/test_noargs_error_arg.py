import unittest
from test.support import cpython_only
import _testcapi
import struct
import collections
import itertools
import gc
import contextlib
import functools
from _testcapi import pyobject_vectorcall, pyvectorcall_call
from types import MethodType
from functools import partial
import test_call

def test_noargs_error_arg():
    msg = 'meth_noargs\\(\\) takes no arguments \\(1 given\\)'
    TestCallingConventions.assertRaisesRegex(TypeError, msg, lambda : TestCallingConventions.obj.meth_noargs(1))

TestCallingConventions = test_call.TestCallingConventions()
test_noargs_error_arg()
