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

@unittest.skipUnless(os.path.altsep, 'requires os.path.altsep')
def test_move_dir_altsep_to_dir():
    TestMove._check_move_dir(TestMove.src_dir + os.path.altsep, TestMove.dst_dir, os.path.join(TestMove.dst_dir, os.path.basename(TestMove.src_dir)))

TestMove = test_shutil.TestMove()
test_move_dir_altsep_to_dir()
