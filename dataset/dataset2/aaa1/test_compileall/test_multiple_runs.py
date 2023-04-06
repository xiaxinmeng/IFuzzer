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

def test_multiple_runs():
    CommandLineTestsBase.assertRunOK('-q', CommandLineTestsBase.pkgdir)
    CommandLineTestsBase.assertTrue(os.path.exists(CommandLineTestsBase.pkgdir_cachedir))
    cachecachedir = os.path.join(CommandLineTestsBase.pkgdir_cachedir, '__pycache__')
    CommandLineTestsBase.assertFalse(os.path.exists(cachecachedir))
    CommandLineTestsBase.assertRunOK('-q', CommandLineTestsBase.pkgdir)
    CommandLineTestsBase.assertTrue(os.path.exists(CommandLineTestsBase.pkgdir_cachedir))
    CommandLineTestsBase.assertFalse(os.path.exists(cachecachedir))

CommandLineTestsBase = test_compileall.CommandLineTestsBase()
test_multiple_runs()
