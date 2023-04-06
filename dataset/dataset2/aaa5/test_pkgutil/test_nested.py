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

def test_nested():
    pkgutil_boilerplate = 'import pkgutil; __path__ = pkgutil.extend_path(__path__, __name__)'
    NestedNamespacePackageTest.create_module('a.pkg.__init__', pkgutil_boilerplate)
    NestedNamespacePackageTest.create_module('b.pkg.__init__', pkgutil_boilerplate)
    NestedNamespacePackageTest.create_module('a.pkg.subpkg.__init__', pkgutil_boilerplate)
    NestedNamespacePackageTest.create_module('b.pkg.subpkg.__init__', pkgutil_boilerplate)
    NestedNamespacePackageTest.create_module('a.pkg.subpkg.c', 'c = 1')
    NestedNamespacePackageTest.create_module('b.pkg.subpkg.d', 'd = 2')
    sys.path.insert(0, os.path.join(NestedNamespacePackageTest.basedir, 'a'))
    sys.path.insert(0, os.path.join(NestedNamespacePackageTest.basedir, 'b'))
    import pkg
    NestedNamespacePackageTest.addCleanup(unload, 'pkg')
    NestedNamespacePackageTest.assertEqual(len(pkg.__path__), 2)
    import pkg.subpkg
    NestedNamespacePackageTest.addCleanup(unload, 'pkg.subpkg')
    NestedNamespacePackageTest.assertEqual(len(pkg.subpkg.__path__), 2)
    from pkg.subpkg.c import c
    from pkg.subpkg.d import d
    NestedNamespacePackageTest.assertEqual(c, 1)
    NestedNamespacePackageTest.assertEqual(d, 2)

NestedNamespacePackageTest = test_pkgutil.NestedNamespacePackageTest()
NestedNamespacePackageTest.setUp()
test_nested()
