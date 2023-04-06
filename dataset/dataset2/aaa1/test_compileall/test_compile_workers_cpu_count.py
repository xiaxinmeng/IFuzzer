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

@mock.patch('concurrent.futures.ProcessPoolExecutor')
def test_compile_workers_cpu_count(CompileallTestsBase, pool_mock):
    compileall.compile_dir(CompileallTestsBase.directory, quiet=True, workers=0)
    CompileallTestsBase.assertEqual(pool_mock.call_args[1]['max_workers'], None)

CompileallTestsBase = test_compileall.CompileallTestsBase()
test_compile_workers_cpu_count()
