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

@os_helper.skip_unless_symlink
def test_cleanup_with_symlink_to_a_directory():
    d1 = TestTemporaryDirectory.do_create()
    d2 = TestTemporaryDirectory.do_create(recurse=0)
    os.symlink(d2.name, os.path.join(d1.name, 'foo'))
    d1.cleanup()
    TestTemporaryDirectory.assertFalse(os.path.exists(d1.name), 'TemporaryDirectory %s exists after cleanup' % d1.name)
    TestTemporaryDirectory.assertTrue(os.path.exists(d2.name), 'Directory pointed to by a symlink was deleted')
    TestTemporaryDirectory.assertEqual(os.listdir(d2.name), ['test0.txt'], 'Contents of the directory pointed to by a symlink were deleted')
    d2.cleanup()

TestTemporaryDirectory = test_tempfile.TestTemporaryDirectory()
test_cleanup_with_symlink_to_a_directory()
