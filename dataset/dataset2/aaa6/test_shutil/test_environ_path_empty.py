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

def test_environ_path_empty():
    with os_helper.EnvironmentVarGuard() as env:
        env['PATH'] = ''
        with unittest.mock.patch('os.confstr', return_value=TestWhich.dir, create=True), support.swap_attr(os, 'defpath', TestWhich.dir), os_helper.change_cwd(TestWhich.dir):
            rv = shutil.which(TestWhich.file)
            TestWhich.assertIsNone(rv)

TestWhich = test_shutil.TestWhich()
TestWhich.setUp()
test_environ_path_empty()
