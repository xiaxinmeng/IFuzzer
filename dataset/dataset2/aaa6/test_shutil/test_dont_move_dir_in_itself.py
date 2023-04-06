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

def test_dont_move_dir_in_itTestMove():
    dst = os.path.join(TestMove.src_dir, 'bar')
    TestMove.assertRaises(shutil.Error, shutil.move, TestMove.src_dir, dst)

TestMove = test_shutil.TestMove()
TestMove.setUp()
test_dont_move_dir_in_itTestMove()