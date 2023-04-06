import functools
import importlib.util
import os
import py_compile
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
from test import support
from test.support import os_helper, script_helper
import test_py_compile

def test_with_files():
    (rc, stdout, stderr) = PyCompileCLITestCase.pycompilecmd(PyCompileCLITestCase.source_path, PyCompileCLITestCase.source_path)
    PyCompileCLITestCase.assertEqual(rc, 0)
    PyCompileCLITestCase.assertEqual(stdout, b'')
    PyCompileCLITestCase.assertEqual(stderr, b'')
    PyCompileCLITestCase.assertTrue(os.path.exists(PyCompileCLITestCase.cache_path))

PyCompileCLITestCase = test_py_compile.PyCompileCLITestCase()
PyCompileCLITestCase.setUp()
test_with_files()
