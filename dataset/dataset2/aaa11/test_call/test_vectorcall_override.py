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

def test_vectorcall_override():
    args = tuple(range(5))
    f = _testcapi.MethodDescriptorNopGet()
    TestPEP590.assertIs(f(*args), args)

TestPEP590 = test_call.TestPEP590()
test_vectorcall_override()
