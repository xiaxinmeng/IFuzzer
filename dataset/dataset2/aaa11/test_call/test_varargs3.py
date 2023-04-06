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

def test_varargs3():
    msg = '^from_bytes\\(\\) takes exactly 2 positional arguments \\(3 given\\)'
    CFunctionCallsErrorMessages.assertRaisesRegex(TypeError, msg, int.from_bytes, b'a', 'little', False)

CFunctionCallsErrorMessages = test_call.CFunctionCallsErrorMessages()
test_varargs3()
