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

def test_file_offset():
    with TestCopyFileObj.get_files() as (src, dst):
        shutil.copyfileobj(src, dst)
        TestCopyFileObj.assertEqual(src.tell(), TestCopyFileObj.FILESIZE)
        TestCopyFileObj.assertEqual(dst.tell(), TestCopyFileObj.FILESIZE)

TestCopyFileObj = test_shutil.TestCopyFileObj()
test_file_offset()
