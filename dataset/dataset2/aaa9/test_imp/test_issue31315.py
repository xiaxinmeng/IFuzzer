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

@support.cpython_only
def test_issue31315():
    create_dynamic = support.get_attribute(imp, 'create_dynamic')

    class BadSpec:
        name = None
        origin = 'foo'
    with ImportTests.assertRaises(TypeError):
        create_dynamic(BadSpec())

ImportTests = test_imp.ImportTests()
test_issue31315()
