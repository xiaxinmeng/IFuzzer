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

def test_stdin():
    result = PyCompileCLITestCase.pycompilecmd('-', input=PyCompileCLITestCase.source_path)
    PyCompileCLITestCase.assertEqual(result.returncode, 0)
    PyCompileCLITestCase.assertEqual(result.stdout, b'')
    PyCompileCLITestCase.assertEqual(result.stderr, b'')
    PyCompileCLITestCase.assertTrue(os.path.exists(PyCompileCLITestCase.cache_path))

PyCompileCLITestCase = test_py_compile.PyCompileCLITestCase()
PyCompileCLITestCase.setUp()
test_stdin()
