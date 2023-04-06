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

def test_module():
    LongReprTest.maxDiff = None
    LongReprTest._check_path_limitations(LongReprTest.pkgname)
    create_empty_file(os.path.join(LongReprTest.subpkgname, LongReprTest.pkgname + '.py'))
    importlib.invalidate_caches()
    from areallylongpackageandmodulenametotestreprtruncation.areallylongpackageandmodulenametotestreprtruncation import areallylongpackageandmodulenametotestreprtruncation
    module = areallylongpackageandmodulenametotestreprtruncation
    LongReprTest.assertEqual(repr(module), '<module %r from %r>' % (module.__name__, module.__file__))
    LongReprTest.assertEqual(repr(sys), "<module 'sys' (built-in)>")

LongReprTest = test_reprlib.LongReprTest()
LongReprTest.setUp()
test_module()
