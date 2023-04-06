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

def test_positional_only_passed_as_keyword():
    msg = "A.positional_only() got some positional-only arguments passed as keyword arguments: 'arg'"
    with TestErrorMessagesUseQualifiedName.check_raises_type_error(msg):
        test_call.A.positional_only(arg='x')

TestErrorMessagesUseQualifiedName = test_call.TestErrorMessagesUseQualifiedName()
test_positional_only_passed_as_keyword()
