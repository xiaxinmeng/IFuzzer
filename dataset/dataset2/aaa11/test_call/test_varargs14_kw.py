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

def test_varargs14_kw():
    msg = '^product\\(\\) takes at most 1 keyword argument \\(2 given\\)$'
    CFunctionCallsErrorMessages.assertRaisesRegex(TypeError, msg, itertools.product, 0, repeat=1, foo=2)

CFunctionCallsErrorMessages = test_call.CFunctionCallsErrorMessages()
test_varargs14_kw()
