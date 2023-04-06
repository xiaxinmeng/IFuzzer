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

@unittest.mock.patch('os.chmod')
def test_copytree_winerror(TestCopyTree, mock_patch):
    src_dir = TestCopyTree.mkdtemp()
    dst_dir = os.path.join(TestCopyTree.mkdtemp(), 'destination')
    TestCopyTree.addCleanup(shutil.rmtree, src_dir)
    TestCopyTree.addCleanup(shutil.rmtree, os.path.dirname(dst_dir))
    mock_patch.side_effect = PermissionError('ka-boom')
    with TestCopyTree.assertRaises(shutil.Error):
        shutil.copytree(src_dir, dst_dir)

TestCopyTree = test_shutil.TestCopyTree()
test_copytree_winerror()
