from test.support import run_unittest
from test.support.import_helper import unload, CleanImport
from test.support.warnings_helper import check_warnings
import unittest
import sys
import importlib
from importlib.util import spec_from_file_location
import pkgutil
import os
import os.path
import tempfile
import shutil
import zipfile
import logging
import logging.handlers

import zipimport
import importlib
import test_pkgutil

def test_getdata_pep302():
    PkgutilPEP302Tests.assertEqual(pkgutil.get_data('foo', 'dummy'), 'Hello, world!')
    del sys.modules['foo']

PkgutilPEP302Tests = test_pkgutil.PkgutilPEP302Tests()
test_getdata_pep302()
