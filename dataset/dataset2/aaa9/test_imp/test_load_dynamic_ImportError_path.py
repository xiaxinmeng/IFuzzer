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

@test_imp.requires_load_dynamic
def test_load_dynamic_ImportError_path():
    path = 'bogus file path'
    name = 'extension'
    with ImportTests.assertRaises(ImportError) as err:
        imp.load_dynamic(name, path)
    ImportTests.assertIn(path, err.exception.path)
    ImportTests.assertEqual(name, err.exception.name)

ImportTests = test_imp.ImportTests()
test_load_dynamic_ImportError_path()
