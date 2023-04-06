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

def test_varargs2min():
    msg = 'getattr expected at least 2 arguments, got 0'
    CFunctionCallsErrorMessages.assertRaisesRegex(TypeError, msg, getattr)

CFunctionCallsErrorMessages = test_call.CFunctionCallsErrorMessages()
test_varargs2min()
