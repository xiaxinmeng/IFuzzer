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

def test_pyc_invalidation_mode():
    script_helper.make_script(CommandLineTestsBase.pkgdir, 'f1', '')
    pyc = importlib.util.cache_from_source(os.path.join(CommandLineTestsBase.pkgdir, 'f1.py'))
    CommandLineTestsBase.assertRunOK('--invalidation-mode=checked-hash', CommandLineTestsBase.pkgdir)
    with open(pyc, 'rb') as fp:
        data = fp.read()
    CommandLineTestsBase.assertEqual(int.from_bytes(data[4:8], 'little'), 3)
    CommandLineTestsBase.assertRunOK('--invalidation-mode=unchecked-hash', CommandLineTestsBase.pkgdir)
    with open(pyc, 'rb') as fp:
        data = fp.read()
    CommandLineTestsBase.assertEqual(int.from_bytes(data[4:8], 'little'), 1)

CommandLineTestsBase = test_compileall.CommandLineTestsBase()
test_pyc_invalidation_mode()
