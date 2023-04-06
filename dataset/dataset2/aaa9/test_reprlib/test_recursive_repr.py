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

def test_recursive_repr():
    m = test_reprlib.MyContainer(list('abcde'))
    m.append(m)
    m.append('x')
    m.append(m)
    TestRecursiveRepr.assertEqual(repr(m), '<a, b, c, d, e, ..., x, ...>')
    m = test_reprlib.MyContainer2(list('abcde'))
    m.append(m)
    m.append('x')
    m.append(m)
    TestRecursiveRepr.assertEqual(repr(m), '<a, b, c, d, e, +++, x, +++>')

TestRecursiveRepr = test_reprlib.TestRecursiveRepr()
test_recursive_repr()
