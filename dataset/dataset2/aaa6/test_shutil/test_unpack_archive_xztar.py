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

@support.requires_lzma()
@unittest.skipIf(test_shutil.AIX and (not _maxdataOK()), 'AIX MAXDATA must be 0x20000000 or larger')
def test_unpack_archive_xztar():
    TestArchives.check_unpack_archive('xztar')

TestArchives = test_shutil.TestArchives()
test_unpack_archive_xztar()
