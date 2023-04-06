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

def test_unreadable_dir_on_syspath():
    package_name = 'unreadable_package'
    d = os.path.join(PkgutilTests.dirname, package_name)
    os.mkdir(d, 0)
    PkgutilTests.addCleanup(os.rmdir, d)
    for t in pkgutil.walk_packages(path=[PkgutilTests.dirname]):
        PkgutilTests.fail('unexpected package found')

PkgutilTests = test_pkgutil.PkgutilTests()
PkgutilTests.setUp()
test_unreadable_dir_on_syspath()
