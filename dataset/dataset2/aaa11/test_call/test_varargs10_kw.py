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

def test_varargs10_kw():
    msg = '^deque[.]index\\(\\) takes no keyword arguments$'
    CFunctionCallsErrorMessages.assertRaisesRegex(TypeError, msg, collections.deque().index, x=2)

CFunctionCallsErrorMessages = test_call.CFunctionCallsErrorMessages()
test_varargs10_kw()
