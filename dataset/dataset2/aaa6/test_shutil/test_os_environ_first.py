import unittest
import unittest.mock
import shutil
import tempfile
import sys
import stat
import os
import os.path
import errno
import functools
import pathlib
import subprocess
import random
import string
import contextlib
import io
from shutil import make_archive, register_archive_format, unregister_archive_format, get_archive_formats, Error, unpack_archive, register_unpack_format, RegistryError, unregister_unpack_format, get_unpack_formats, SameFileError, _GiveupOnFastCopy
import tarfile
import zipfile
import posix
from test import support
from test.support import os_helper
from test.support.os_helper import TESTFN, FakePath
import grp
import pwd

import test_shutil

def test_os_environ_first():
    """Check if environment variables have precedence"""
    with os_helper.EnvironmentVarGuard() as env:
        env['COLUMNS'] = '777'
        del env['LINES']
        size = shutil.get_terminal_size()
    TestGetTerminalSize.assertEqual(size.columns, 777)
    with os_helper.EnvironmentVarGuard() as env:
        del env['COLUMNS']
        env['LINES'] = '888'
        size = shutil.get_terminal_size()
    TestGetTerminalSize.assertEqual(size.lines, 888)

TestGetTerminalSize = test_shutil.TestGetTerminalSize()
test_os_environ_first()
