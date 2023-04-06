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

@mock.patch('concurrent.futures.ProcessPoolExecutor', new=None)
@mock.patch('compileall.compile_file')
def test_compile_missing_multiprocessing(CompileallTestsBase, compile_file_mock):
    compileall.compile_dir(CompileallTestsBase.directory, quiet=True, workers=5)
    CompileallTestsBase.assertTrue(compile_file_mock.called)

CompileallTestsBase = test_compileall.CompileallTestsBase()
CompileallTestsBase.setUp()
test_compile_missing_multiprocessing()
