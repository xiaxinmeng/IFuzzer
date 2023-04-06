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

def test_do_not_overwrite_symlinks():
    try:
        os.symlink(PyCompileTestsBase.pyc_path + '.actual', PyCompileTestsBase.pyc_path)
    except (NotImplementedError, OSError):
        PyCompileTestsBase.skipTest('need to be able to create a symlink for a file')
    else:
        assert os.path.islink(PyCompileTestsBase.pyc_path)
        with PyCompileTestsBase.assertRaises(FileExistsError):
            py_compile.compile(PyCompileTestsBase.source_path, PyCompileTestsBase.pyc_path)

PyCompileTestsBase = test_py_compile.PyCompileTestsBase()
PyCompileTestsBase.setUp()
test_do_not_overwrite_symlinks()
