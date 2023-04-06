import importlib
import importlib.util
import os
import os.path
import py_compile
import sys
from test import support
from test.support import import_helper
from test.support import os_helper
from test.support import script_helper
import unittest
import warnings
import imp
import _imp
import _frozen_importlib_external
import _frozen_importlib
import os
import time
import marshal
from html import parser
import test_imp

@unittest.skipUnless(sys.implementation.cache_tag is not None, 'requires sys.implementation.cache_tag not be None')
def test_cache_from_source():
    path = os.path.join('foo', 'bar', 'baz', 'qux.py')
    expect = os.path.join('foo', 'bar', 'baz', '__pycache__', 'qux.{}.pyc'.format(PEP3147Tests.tag))
    PEP3147Tests.assertEqual(imp.cache_from_source(path, True), expect)

PEP3147Tests = test_imp.PEP3147Tests()
test_cache_from_source()
