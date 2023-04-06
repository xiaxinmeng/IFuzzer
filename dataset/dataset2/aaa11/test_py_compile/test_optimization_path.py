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

def test_optimization_path():
    PyCompileTestsBase.assertIn('opt-2', py_compile.compile(PyCompileTestsBase.source_path, optimize=2))

PyCompileTestsBase = test_py_compile.PyCompileTestsBase()
test_optimization_path()
