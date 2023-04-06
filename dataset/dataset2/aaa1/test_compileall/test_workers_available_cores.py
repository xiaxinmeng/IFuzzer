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

@mock.patch('compileall.compile_dir')
def test_workers_available_cores(CommandLineTestsBase, compile_dir):
    with mock.patch('sys.argv', new=[sys.executable, CommandLineTestsBase.directory, '-j0']):
        compileall.main()
        CommandLineTestsBase.assertTrue(compile_dir.called)
        CommandLineTestsBase.assertEqual(compile_dir.call_args[-1]['workers'], 0)

CommandLineTestsBase = test_compileall.CommandLineTestsBase()
test_workers_available_cores()
