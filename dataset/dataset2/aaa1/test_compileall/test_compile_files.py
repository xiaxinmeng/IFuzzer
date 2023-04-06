import compileall
import contextlib
import filecmp
import importlib.util
import io
import itertools
import os
import pathlib
import py_compile
import shutil
import struct
import sys
import tempfile
import test.test_importlib.util
import time
import unittest
from unittest import mock, skipUnless
from concurrent.futures import ProcessPoolExecutor
from test import support
from test.support import os_helper
from test.support import script_helper

import test_compileall

def test_compile_files():
    for fn in (CompileallTestsBase.bc_path, CompileallTestsBase.bc_path2):
        try:
            os.unlink(fn)
        except:
            pass
    CompileallTestsBase.assertTrue(compileall.compile_file(CompileallTestsBase.source_path, force=False, quiet=True))
    CompileallTestsBase.assertTrue(os.path.isfile(CompileallTestsBase.bc_path) and (not os.path.isfile(CompileallTestsBase.bc_path2)))
    os.unlink(CompileallTestsBase.bc_path)
    CompileallTestsBase.assertTrue(compileall.compile_dir(CompileallTestsBase.directory, force=False, quiet=True))
    CompileallTestsBase.assertTrue(os.path.isfile(CompileallTestsBase.bc_path) and os.path.isfile(CompileallTestsBase.bc_path2))
    os.unlink(CompileallTestsBase.bc_path)
    os.unlink(CompileallTestsBase.bc_path2)
    CompileallTestsBase.add_bad_source_file()
    CompileallTestsBase.assertFalse(compileall.compile_file(CompileallTestsBase.bad_source_path, force=False, quiet=2))
    CompileallTestsBase.assertFalse(compileall.compile_dir(CompileallTestsBase.directory, force=False, quiet=2))

CompileallTestsBase = test_compileall.CompileallTestsBase()
CompileallTestsBase.setUp()
test_compile_files()
