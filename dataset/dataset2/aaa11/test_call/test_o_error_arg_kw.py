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

def test_o_error_arg_kw():
    msg = 'meth_o\\(\\) takes no keyword arguments'
    TestCallingConventions.assertRaisesRegex(TypeError, msg, lambda : TestCallingConventions.obj.meth_o(k=1))

TestCallingConventions = test_call.TestCallingConventions()
test_o_error_arg_kw()
