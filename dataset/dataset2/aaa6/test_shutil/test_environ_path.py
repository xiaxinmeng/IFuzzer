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

def test_environ_path():
    with os_helper.EnvironmentVarGuard() as env:
        env['PATH'] = TestWhich.env_path
        rv = shutil.which(TestWhich.file)
        TestWhich.assertEqual(rv, TestWhich.temp_file.name)

TestWhich = test_shutil.TestWhich()
TestWhich.setUp()
test_environ_path()
