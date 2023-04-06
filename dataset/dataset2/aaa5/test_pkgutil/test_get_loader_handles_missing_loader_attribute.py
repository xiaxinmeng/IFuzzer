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

@unittest.skipIf(__name__ == '__main__', 'not compatible with __main__')
def test_get_loader_handles_missing_loader_attribute():
    global __loader__
    this_loader = __loader__
    del __loader__
    try:
        with check_warnings() as w:
            ImportlibMigrationTests.assertIsNotNone(pkgutil.get_loader(__name__))
            ImportlibMigrationTests.assertEqual(len(w.warnings), 0)
    finally:
        __loader__ = this_loader

ImportlibMigrationTests = test_pkgutil.ImportlibMigrationTests()
test_get_loader_handles_missing_loader_attribute()
