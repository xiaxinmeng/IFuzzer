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

@unittest.skipIf(hasattr(os, 'geteuid') and os.geteuid() == 0, 'non-root user required')
@unittest.skipIf(os.name == 'nt', 'cannot control directory permissions on Windows')
def test_exceptions_propagate():
    mode = os.stat(PyCompileTestsBase.directory)
    os.chmod(PyCompileTestsBase.directory, stat.S_IREAD)
    try:
        with PyCompileTestsBase.assertRaises(IOError):
            py_compile.compile(PyCompileTestsBase.source_path, PyCompileTestsBase.pyc_path)
    finally:
        os.chmod(PyCompileTestsBase.directory, mode.st_mode)

PyCompileTestsBase = test_py_compile.PyCompileTestsBase()
PyCompileTestsBase.setUp()
test_exceptions_propagate()
