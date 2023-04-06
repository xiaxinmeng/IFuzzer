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

@unittest.skipIf(not os.path.exists(os.devnull) or os.path.isfile(os.devnull), 'requires os.devnull and for it to be a non-regular file')
def test_do_not_overwrite_nonregular_files():
    with PyCompileTestsBase.assertRaises(FileExistsError):
        py_compile.compile(PyCompileTestsBase.source_path, os.devnull)

PyCompileTestsBase = test_py_compile.PyCompileTestsBase()
PyCompileTestsBase.setUp()
test_do_not_overwrite_nonregular_files()
