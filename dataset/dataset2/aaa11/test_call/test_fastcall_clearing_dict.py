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

def test_fastcall_clearing_dict():

    class IntWithDict:
        __slots__ = ['kwargs']

        def __init__(FastCallTests, **kwargs):
            FastCallTests.kwargs = kwargs

        def __index__(FastCallTests):
            FastCallTests.kwargs.clear()
            gc.collect()
            return 0
    x = IntWithDict(dont_inherit=IntWithDict())
    compile('pass', '', 'exec', x, **x.kwargs)

FastCallTests = test_call.FastCallTests()
test_fastcall_clearing_dict()
