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

def test_set_literal():
    eq = ReprTests.assertEqual
    eq(r({1}), '{1}')
    eq(r({1, 2, 3}), '{1, 2, 3}')
    eq(r({1, 2, 3, 4, 5, 6}), '{1, 2, 3, 4, 5, 6}')
    eq(r({1, 2, 3, 4, 5, 6, 7}), '{1, 2, 3, 4, 5, 6, ...}')

ReprTests = test_reprlib.ReprTests()
test_set_literal()
