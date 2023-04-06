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

def test_module_all_attribute():
    PublicAPITests.assertTrue(hasattr(shutil, '__all__'))
    target_api = ['copyfileobj', 'copyfile', 'copymode', 'copystat', 'copy', 'copy2', 'copytree', 'move', 'rmtree', 'Error', 'SpecialFileError', 'ExecError', 'make_archive', 'get_archive_formats', 'register_archive_format', 'unregister_archive_format', 'get_unpack_formats', 'register_unpack_format', 'unregister_unpack_format', 'unpack_archive', 'ignore_patterns', 'chown', 'which', 'get_terminal_size', 'SameFileError']
    if hasattr(os, 'statvfs') or os.name == 'nt':
        target_api.append('disk_usage')
    PublicAPITests.assertEqual(set(shutil.__all__), set(target_api))

PublicAPITests = test_shutil.PublicAPITests()
test_module_all_attribute()
