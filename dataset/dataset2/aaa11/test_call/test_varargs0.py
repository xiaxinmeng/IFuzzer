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

def test_varargs0():
    msg = '__contains__\\(\\) takes exactly one argument \\(0 given\\)'
    CFunctionCallsErrorMessages.assertRaisesRegex(TypeError, msg, {}.__contains__)

CFunctionCallsErrorMessages = test_call.CFunctionCallsErrorMessages()
test_varargs0()
