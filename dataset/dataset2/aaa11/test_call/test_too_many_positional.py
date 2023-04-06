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

def test_too_many_positional():
    msg = 'A.static_no_args() takes 0 positional arguments but 1 was given'
    with TestErrorMessagesUseQualifiedName.check_raises_type_error(msg):
        test_call.A.static_no_args("oops it's an arg")

TestErrorMessagesUseQualifiedName = test_call.TestErrorMessagesUseQualifiedName()
test_too_many_positional()
