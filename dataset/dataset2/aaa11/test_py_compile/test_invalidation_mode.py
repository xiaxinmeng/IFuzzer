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

def test_invalidation_mode():
    py_compile.compile(PyCompileTestsBase.source_path, invalidation_mode=py_compile.PycInvalidationMode.CHECKED_HASH)
    with open(PyCompileTestsBase.cache_path, 'rb') as fp:
        flags = importlib._bootstrap_external._classify_pyc(fp.read(), 'test', {})
    PyCompileTestsBase.assertEqual(flags, 3)
    py_compile.compile(PyCompileTestsBase.source_path, invalidation_mode=py_compile.PycInvalidationMode.UNCHECKED_HASH)
    with open(PyCompileTestsBase.cache_path, 'rb') as fp:
        flags = importlib._bootstrap_external._classify_pyc(fp.read(), 'test', {})
    PyCompileTestsBase.assertEqual(flags, 1)

PyCompileTestsBase = test_py_compile.PyCompileTestsBase()
test_invalidation_mode()
