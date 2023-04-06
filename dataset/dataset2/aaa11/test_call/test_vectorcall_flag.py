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

def test_vectorcall_flag():
    TestPEP590.assertTrue(_testcapi.MethodDescriptorBase.__flags__ & test_call.Py_TPFLAGS_HAVE_VECTORCALL)
    TestPEP590.assertTrue(_testcapi.MethodDescriptorDerived.__flags__ & test_call.Py_TPFLAGS_HAVE_VECTORCALL)
    TestPEP590.assertFalse(_testcapi.MethodDescriptorNopGet.__flags__ & test_call.Py_TPFLAGS_HAVE_VECTORCALL)
    TestPEP590.assertTrue(_testcapi.MethodDescriptor2.__flags__ & test_call.Py_TPFLAGS_HAVE_VECTORCALL)

    class MethodDescriptorHeap(_testcapi.MethodDescriptorBase):
        pass
    TestPEP590.assertFalse(MethodDescriptorHeap.__flags__ & test_call.Py_TPFLAGS_HAVE_VECTORCALL)

TestPEP590 = test_call.TestPEP590()
test_vectorcall_flag()
