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
def test_load_module_extension_file_is_None():
    name = '_testimportmultiple'
    found = imp.find_module(name)
    if found[0] is not None:
        found[0].close()
    if found[2][2] != imp.C_EXTENSION:
        ImportTests.skipTest("found module doesn't appear to be a C extension")
    imp.load_module(name, None, *found[1:])

ImportTests = test_imp.ImportTests()
test_load_module_extension_file_is_None()
