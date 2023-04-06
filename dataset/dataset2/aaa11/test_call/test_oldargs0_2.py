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

def test_oldargs0_2():
    msg = 'keys\\(\\) takes no arguments \\(2 given\\)'
    CFunctionCallsErrorMessages.assertRaisesRegex(TypeError, msg, {}.keys, 0, 1)

CFunctionCallsErrorMessages = test_call.CFunctionCallsErrorMessages()
test_oldargs0_2()
