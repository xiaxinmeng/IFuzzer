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

def test_varargs9_kw():
    msg = '^_struct[.]pack_into\\(\\) takes no keyword arguments$'
    CFunctionCallsErrorMessages.assertRaisesRegex(TypeError, msg, struct.pack_into, x=2)

CFunctionCallsErrorMessages = test_call.CFunctionCallsErrorMessages()
test_varargs9_kw()
