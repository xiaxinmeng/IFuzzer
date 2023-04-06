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

def test_noargs():
    TestCallingConventions.assertEqual(TestCallingConventions.obj.meth_noargs(), TestCallingConventions.expected_TestCallingConventions)

TestCallingConventions = test_call.TestCallingConventions()
test_noargs()
