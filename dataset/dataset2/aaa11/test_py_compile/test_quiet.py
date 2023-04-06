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

def test_quiet():
    bad_coding = os.path.join(os.path.dirname(__file__), 'bad_coding2.py')
    with support.captured_stderr() as stderr:
        PyCompileTestsBase.assertIsNone(py_compile.compile(bad_coding, doraise=False, quiet=2))
        PyCompileTestsBase.assertIsNone(py_compile.compile(bad_coding, doraise=True, quiet=2))
        PyCompileTestsBase.assertEqual(stderr.getvalue(), '')
        with PyCompileTestsBase.assertRaises(py_compile.PyCompileError):
            py_compile.compile(bad_coding, doraise=True, quiet=1)

PyCompileTestsBase = test_py_compile.PyCompileTestsBase()
PyCompileTestsBase.setUp()
test_quiet()
