import inspect
import sys
import threading
import unittest
import weakref
import ctypes
from test.support import run_doctest, run_unittest, cpython_only, check_impl_detail
import _testcapi
from types import FunctionType
from test import test_code
import test_code

@cpython_only
def test_interned_string():
    co = compile('res = "str_value"', '?', 'exec')
    v = CodeConstsTest.find_const(co.co_consts, 'str_value')
    CodeConstsTest.assertIsInterned(v)

CodeConstsTest = test_code.CodeConstsTest()
test_interned_string()
