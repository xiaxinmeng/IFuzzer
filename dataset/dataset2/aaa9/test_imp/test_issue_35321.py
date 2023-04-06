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

def test_issue_35321():
    import _frozen_importlib_external
    ImportTests.assertEqual(_frozen_importlib_external.__spec__.origin, 'frozen')
    import _frozen_importlib
    ImportTests.assertEqual(_frozen_importlib.__spec__.origin, 'frozen')

ImportTests = test_imp.ImportTests()
test_issue_35321()
