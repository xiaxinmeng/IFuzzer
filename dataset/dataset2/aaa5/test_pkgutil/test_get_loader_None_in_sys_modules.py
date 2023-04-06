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

def test_get_loader_None_in_sys_modules():
    name = 'totally bogus'
    sys.modules[name] = None
    try:
        loader = pkgutil.get_loader(name)
    finally:
        del sys.modules[name]
    ImportlibMigrationTests.assertIsNone(loader)

ImportlibMigrationTests = test_pkgutil.ImportlibMigrationTests()
test_get_loader_None_in_sys_modules()
