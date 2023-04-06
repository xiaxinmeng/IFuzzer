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

def test_cwd():
    with os_helper.change_cwd(PyCompileTestsBase.directory):
        py_compile.compile(os.path.basename(PyCompileTestsBase.source_path), os.path.basename(PyCompileTestsBase.pyc_path))
    PyCompileTestsBase.assertTrue(os.path.exists(PyCompileTestsBase.pyc_path))
    PyCompileTestsBase.assertFalse(os.path.exists(PyCompileTestsBase.cache_path))

PyCompileTestsBase = test_py_compile.PyCompileTestsBase()
PyCompileTestsBase.setUp()
test_cwd()
