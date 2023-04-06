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

def test_compile_file_pathlike_ddir():
    CompileallTestsBase.assertFalse(os.path.isfile(CompileallTestsBase.bc_path))
    CompileallTestsBase.assertTrue(compileall.compile_file(pathlib.Path(CompileallTestsBase.source_path), ddir=pathlib.Path('ddir_path'), quiet=2))
    CompileallTestsBase.assertTrue(os.path.isfile(CompileallTestsBase.bc_path))

CompileallTestsBase = test_compileall.CompileallTestsBase()
CompileallTestsBase.setUp()
test_compile_file_pathlike_ddir()
