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

def test_empty_path():
    base_dir = os.path.dirname(TestWhich.dir)
    with os_helper.change_cwd(path=TestWhich.dir), os_helper.EnvironmentVarGuard() as env:
        env['PATH'] = TestWhich.env_path
        rv = shutil.which(TestWhich.file, path='')
        TestWhich.assertIsNone(rv)

TestWhich = test_shutil.TestWhich()
TestWhich.setUp()
test_empty_path()
