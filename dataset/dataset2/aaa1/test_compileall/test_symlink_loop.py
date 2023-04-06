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

@os_helper.skip_unless_symlink
def test_symlink_loop():
    pkg = os.path.join(CommandLineTestsBase.pkgdir, 'spam')
    script_helper.make_pkg(pkg)
    os.symlink('.', os.path.join(pkg, 'evil'))
    os.symlink('.', os.path.join(pkg, 'evil2'))
    CommandLineTestsBase.assertRunOK('-q', CommandLineTestsBase.pkgdir)
    CommandLineTestsBase.assertCompiled(os.path.join(CommandLineTestsBase.pkgdir, 'spam', 'evil', 'evil2', '__init__.py'))

CommandLineTestsBase = test_compileall.CommandLineTestsBase()
test_symlink_loop()
