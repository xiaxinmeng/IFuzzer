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

def test_source():
    with os_helper.EnvironmentVarGuard():
        import os
        imp.reload(os)

ReloadTests = test_imp.ReloadTests()
test_source()
