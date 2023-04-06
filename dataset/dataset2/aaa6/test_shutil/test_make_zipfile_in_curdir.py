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

@support.requires_zlib()
def test_make_zipfile_in_curdir():
    root_dir = TestArchives.mkdtemp()
    with os_helper.change_cwd(root_dir):
        TestArchives.assertEqual(make_archive('test', 'zip'), 'test.zip')
        TestArchives.assertTrue(os.path.isfile('test.zip'))

TestArchives = test_shutil.TestArchives()
test_make_zipfile_in_curdir()
