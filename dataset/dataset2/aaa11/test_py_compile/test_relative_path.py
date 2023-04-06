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

def test_relative_path():
    py_compile.compile(os.path.relpath(PyCompileTestsBase.source_path), os.path.relpath(PyCompileTestsBase.pyc_path))
    PyCompileTestsBase.assertTrue(os.path.exists(PyCompileTestsBase.pyc_path))
    PyCompileTestsBase.assertFalse(os.path.exists(PyCompileTestsBase.cache_path))

PyCompileTestsBase = test_py_compile.PyCompileTestsBase()
PyCompileTestsBase.setUp()
test_relative_path()
