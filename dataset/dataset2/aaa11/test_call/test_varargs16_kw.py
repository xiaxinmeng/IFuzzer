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

def test_varargs16_kw():
    msg = '^min\\(\\) takes at most 2 keyword arguments \\(3 given\\)$'
    CFunctionCallsErrorMessages.assertRaisesRegex(TypeError, msg, min, 0, default=1, key=2, foo=3)

CFunctionCallsErrorMessages = test_call.CFunctionCallsErrorMessages()
test_varargs16_kw()
