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

def test_cant_get_size():
    with unittest.mock.patch('os.fstat', side_effect=OSError) as m:
        with TestZeroCopySendfile.get_files() as (src, dst):
            shutil._fastcopy_sendfile(src, dst)
            assert m.called
    TestZeroCopySendfile.assertEqual(read_file(TESTFN2, binary=True), TestZeroCopySendfile.FILEDATA)

TestZeroCopySendfile = test_shutil.TestZeroCopySendfile()
test_cant_get_size()
