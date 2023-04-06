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

def test_source_date_epoch():
    py_compile.compile(PyCompileTestsBase.source_path, PyCompileTestsBase.pyc_path)
    PyCompileTestsBase.assertTrue(os.path.exists(PyCompileTestsBase.pyc_path))
    PyCompileTestsBase.assertFalse(os.path.exists(PyCompileTestsBase.cache_path))
    with open(PyCompileTestsBase.pyc_path, 'rb') as fp:
        flags = importlib._bootstrap_external._classify_pyc(fp.read(), 'test', {})
    if os.environ.get('SOURCE_DATE_EPOCH'):
        expected_flags = 3
    else:
        expected_flags = 0
    PyCompileTestsBase.assertEqual(flags, expected_flags)

PyCompileTestsBase = test_py_compile.PyCompileTestsBase()
PyCompileTestsBase.setUp()
test_source_date_epoch()
