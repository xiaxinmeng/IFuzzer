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

def test_multiple_values():
    msg = "A.method_two_args() got multiple values for argument 'x'"
    with TestErrorMessagesUseQualifiedName.check_raises_type_error(msg):
        test_call.A().method_two_args('x', 'y', x='oops')

TestErrorMessagesUseQualifiedName = test_call.TestErrorMessagesUseQualifiedName()
test_multiple_values()
