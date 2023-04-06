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

@os_helper.skip_unless_symlink
@test_shutil.mock_rename
def test_move_file_symlink_to_dir():
    filename = 'bar'
    dst = os.path.join(TestMove.src_dir, filename)
    os.symlink(TestMove.src_file, dst)
    shutil.move(dst, TestMove.dst_dir)
    final_link = os.path.join(TestMove.dst_dir, filename)
    TestMove.assertTrue(os.path.islink(final_link))
    TestMove.assertTrue(os.path.samefile(TestMove.src_file, final_link))

TestMove = test_shutil.TestMove()
TestMove.setUp()
test_move_file_symlink_to_dir()
