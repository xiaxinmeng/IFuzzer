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

def test_varargs17_kw():
    msg = '^print\\(\\) takes at most 4 keyword arguments \\(5 given\\)$'
    CFunctionCallsErrorMessages.assertRaisesRegex(TypeError, msg, print, 0, sep=1, end=2, file=3, flush=4, foo=5)

CFunctionCallsErrorMessages = test_call.CFunctionCallsErrorMessages()
test_varargs17_kw()
