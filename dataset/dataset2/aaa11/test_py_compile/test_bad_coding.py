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

def test_bad_coding():
    bad_coding = os.path.join(os.path.dirname(__file__), 'bad_coding2.py')
    with support.captured_stderr():
        PyCompileTestsBase.assertIsNone(py_compile.compile(bad_coding, doraise=False))
    PyCompileTestsBase.assertFalse(os.path.exists(importlib.util.cache_from_source(bad_coding)))

PyCompileTestsBase = test_py_compile.PyCompileTestsBase()
PyCompileTestsBase.setUp()
test_bad_coding()
