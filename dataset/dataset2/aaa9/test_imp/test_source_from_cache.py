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

@unittest.skipUnless(sys.implementation.cache_tag is not None, 'requires sys.implementation.cache_tag to not be None')
def test_source_from_cache():
    path = os.path.join('foo', 'bar', 'baz', '__pycache__', 'qux.{}.pyc'.format(PEP3147Tests.tag))
    expect = os.path.join('foo', 'bar', 'baz', 'qux.py')
    PEP3147Tests.assertEqual(imp.source_from_cache(path), expect)

PEP3147Tests = test_imp.PEP3147Tests()
test_source_from_cache()
