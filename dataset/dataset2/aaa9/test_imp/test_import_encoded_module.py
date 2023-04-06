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

def test_import_encoded_module():
    for (modname, encoding, teststr) in ImportTests.test_strings:
        mod = importlib.import_module('test.encoded_modules.module_' + modname)
        ImportTests.assertEqual(teststr, mod.test)

ImportTests = test_imp.ImportTests()
ImportTests.setUp()
test_import_encoded_module()
