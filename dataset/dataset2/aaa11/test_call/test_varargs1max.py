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

def test_varargs1max():
    msg = 'input expected at most 1 argument, got 2'
    CFunctionCallsErrorMessages.assertRaisesRegex(TypeError, msg, input, 1, 2)

CFunctionCallsErrorMessages = test_call.CFunctionCallsErrorMessages()
test_varargs1max()
