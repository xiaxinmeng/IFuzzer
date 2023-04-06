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

def test_walk_packages_raises_on_string_or_bytes_input():
    str_input = 'test_dir'
    with PkgutilTests.assertRaises((TypeError, ValueError)):
        list(pkgutil.walk_packages(str_input))
    bytes_input = b'test_dir'
    with PkgutilTests.assertRaises((TypeError, ValueError)):
        list(pkgutil.walk_packages(bytes_input))

PkgutilTests = test_pkgutil.PkgutilTests()
PkgutilTests.setUp()
test_walk_packages_raises_on_string_or_bytes_input()
