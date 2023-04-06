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

def test_basic():
    namespace = {}
    exec('def f(): pass', globals(), namespace)
    f = namespace['f']
    del namespace
    CodeWeakRefTest.called = False

    def callback(code):
        CodeWeakRefTest.called = True
    coderef = weakref.ref(f.__code__, callback)
    CodeWeakRefTest.assertTrue(bool(coderef()))
    del f
    CodeWeakRefTest.assertFalse(bool(coderef()))
    CodeWeakRefTest.assertTrue(CodeWeakRefTest.called)

CodeWeakRefTest = test_code.CodeWeakRefTest()
test_basic()
