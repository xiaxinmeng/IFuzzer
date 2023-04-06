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

def test_varargs_error_kw():
    msg = 'meth_varargs\\(\\) takes no keyword arguments'
    TestCallingConventions.assertRaisesRegex(TypeError, msg, lambda : TestCallingConventions.obj.meth_varargs(k=1))

TestCallingConventions = test_call.TestCallingConventions()
test_varargs_error_kw()
