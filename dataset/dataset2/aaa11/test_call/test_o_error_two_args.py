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

def test_o_error_two_args():
    msg = 'meth_o\\(\\) takes exactly one argument \\(2 given\\)'
    TestCallingConventions.assertRaisesRegex(TypeError, msg, lambda : TestCallingConventions.obj.meth_o(1, 2))

TestCallingConventions = test_call.TestCallingConventions()
test_o_error_two_args()
