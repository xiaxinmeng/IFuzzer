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

def test_range():
    eq = ReprTests.assertEqual
    eq(repr(range(1)), 'range(0, 1)')
    eq(repr(range(1, 2)), 'range(1, 2)')
    eq(repr(range(1, 4, 3)), 'range(1, 4, 3)')

ReprTests = test_reprlib.ReprTests()
test_range()
