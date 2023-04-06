import sys
import os
import shutil
import importlib
import importlib.util
import unittest
from test.support import verbose
from test.support.os_helper import create_empty_file
from reprlib import repr as r
from reprlib import Repr
from reprlib import recursive_repr
from array import array
from collections import deque

from functools import WRAPPER_ASSIGNMENTS as assigned
import test_reprlib

def test_descriptors():
    eq = ReprTests.assertEqual
    eq(repr(dict.items), "<method 'items' of 'dict' objects>")

    class C:

        def foo(cls):
            pass
    x = staticmethod(C.foo)
    ReprTests.assertTrue(repr(x).startswith('<staticmethod object at 0x'))
    x = classmethod(C.foo)
    ReprTests.assertTrue(repr(x).startswith('<classmethod object at 0x'))

ReprTests = test_reprlib.ReprTests()
test_descriptors()
