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

import _frozen_importlib_external
import _frozen_importlib
import os
import time
import marshal
from html import parser
import test_imp

@unittest.skipIf(sys.dont_write_bytecode, 'test meaningful only when writing bytecode')
def test_bug7732():
    with os_helper.temp_cwd():
        source = os_helper.TESTFN + '.py'
        os.mkdir(source)
        ImportTests.assertRaisesRegex(ImportError, '^No module', imp.find_module, os_helper.TESTFN, ['.'])

ImportTests = test_imp.ImportTests()
test_bug7732()
