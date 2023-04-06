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

def test_no_args_respects_quiet_flag():
    CommandLineTestsBase._skip_if_sys_path_not_writable()
    script_helper.make_script(CommandLineTestsBase.directory, 'baz', '')
    noisy = CommandLineTestsBase.assertRunOK(PYTHONPATH=CommandLineTestsBase.directory)
    CommandLineTestsBase.assertIn(b'Listing ', noisy)
    quiet = CommandLineTestsBase.assertRunOK('-q', PYTHONPATH=CommandLineTestsBase.directory)
    CommandLineTestsBase.assertNotIn(b'Listing ', quiet)

CommandLineTestsBase = test_compileall.CommandLineTestsBase()
test_no_args_respects_quiet_flag()
