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

def test_varargs1min():
    msg = 'get expected at least 1 argument, got 0'
    CFunctionCallsErrorMessages.assertRaisesRegex(TypeError, msg, {}.get)
    msg = 'expected 1 argument, got 0'
    CFunctionCallsErrorMessages.assertRaisesRegex(TypeError, msg, {}.__delattr__)

CFunctionCallsErrorMessages = test_call.CFunctionCallsErrorMessages()
test_varargs1min()
