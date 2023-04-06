import tempfile
import errno
import io
import os
import pathlib
import sys
import re
import warnings
import contextlib
import stat
import types
import weakref
from unittest import mock
import unittest
from test import support
from test.support import os_helper
from test.support import script_helper
from test.support import warnings_helper
import test_tempfile

def test_directory_exists():
    for d in (tempfile.gettempdir(), tempfile.gettempdirb()):
        TestGetTempDir.assertTrue(os.path.isabs(d) or d == os.curdir, '%r is not an absolute path' % d)
        TestGetTempDir.assertTrue(os.path.isdir(d), '%r is not a directory' % d)

TestGetTempDir = test_tempfile.TestGetTempDir()
test_directory_exists()
