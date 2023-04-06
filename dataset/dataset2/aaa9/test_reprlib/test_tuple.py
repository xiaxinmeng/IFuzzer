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

def test_tuple():
    eq = ReprTests.assertEqual
    eq(r((1,)), '(1,)')
    t3 = (1, 2, 3)
    eq(r(t3), '(1, 2, 3)')
    r2 = Repr()
    r2.maxtuple = 2
    expected = repr(t3)[:-2] + '...)'
    eq(r2.repr(t3), expected)

ReprTests = test_reprlib.ReprTests()
test_tuple()
