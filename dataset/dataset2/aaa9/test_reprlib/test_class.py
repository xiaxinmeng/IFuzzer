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

def test_class():
    LongReprTest._check_path_limitations('bar')
    test_reprlib.write_file(os.path.join(LongReprTest.subpkgname, 'bar.py'), 'class bar:\n    pass\n')
    importlib.invalidate_caches()
    from areallylongpackageandmodulenametotestreprtruncation.areallylongpackageandmodulenametotestreprtruncation import bar
    LongReprTest.assertEqual(repr(bar.bar), "<class '%s.bar'>" % bar.__name__)

LongReprTest = test_reprlib.LongReprTest()
LongReprTest.setUp()
test_class()
