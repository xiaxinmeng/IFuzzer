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

def test_compile_path():
    with test.test_importlib.util.import_state(path=[CompileallTestsBase.directory]):
        CompileallTestsBase.assertTrue(compileall.compile_path(quiet=2))
    with test.test_importlib.util.import_state(path=[CompileallTestsBase.directory]):
        CompileallTestsBase.add_bad_source_file()
        CompileallTestsBase.assertFalse(compileall.compile_path(skip_curdir=False, force=True, quiet=2))

CompileallTestsBase = test_compileall.CompileallTestsBase()
CompileallTestsBase.setUp()
test_compile_path()
