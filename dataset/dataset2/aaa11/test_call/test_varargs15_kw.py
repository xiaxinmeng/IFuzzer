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

def test_varargs15_kw():
    msg = '^ImportError\\(\\) takes at most 2 keyword arguments \\(3 given\\)$'
    CFunctionCallsErrorMessages.assertRaisesRegex(TypeError, msg, ImportError, 0, name=1, path=2, foo=3)

CFunctionCallsErrorMessages = test_call.CFunctionCallsErrorMessages()
test_varargs15_kw()
