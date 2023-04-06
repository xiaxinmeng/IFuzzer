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

def test_numbers():
    eq = ReprTests.assertEqual
    eq(r(123), repr(123))
    eq(r(123), repr(123))
    eq(r(1.0 / 3), repr(1.0 / 3))
    n = 10 ** 100
    expected = repr(n)[:18] + '...' + repr(n)[-19:]
    eq(r(n), expected)

ReprTests = test_reprlib.ReprTests()
test_numbers()
