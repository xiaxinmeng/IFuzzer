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

def test_varargs2max():
    msg = 'get expected at most 2 arguments, got 3'
    CFunctionCallsErrorMessages.assertRaisesRegex(TypeError, msg, {}.get, 1, 2, 3)

CFunctionCallsErrorMessages = test_call.CFunctionCallsErrorMessages()
test_varargs2max()
