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

def test_include_bad_file():
    (rc, out, err) = CommandLineTestsBase.assertRunNotOK('-i', os.path.join(CommandLineTestsBase.directory, 'nosuchfile'), CommandLineTestsBase.pkgdir)
    CommandLineTestsBase.assertRegex(out, b'rror.*nosuchfile')
    CommandLineTestsBase.assertNotRegex(err, b'Traceback')
    CommandLineTestsBase.assertFalse(os.path.exists(importlib.util.cache_from_source(CommandLineTestsBase.pkgdir_cachedir)))

CommandLineTestsBase = test_compileall.CommandLineTestsBase()
test_include_bad_file()
