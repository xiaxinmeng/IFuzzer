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
def test_newempty():
    import _testcapi
    co = _testcapi.code_newempty('filename', 'funcname', 15)
    CodeTest.assertEqual(co.co_filename, 'filename')
    CodeTest.assertEqual(co.co_name, 'funcname')
    CodeTest.assertEqual(co.co_firstlineno, 15)

CodeTest = test_code.CodeTest()
test_newempty()
