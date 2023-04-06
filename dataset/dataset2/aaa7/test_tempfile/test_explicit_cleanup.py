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

def test_explicit_cleanup():
    dir = tempfile.mkdtemp()
    try:
        d = TestTemporaryDirectory.do_create(dir=dir)
        TestTemporaryDirectory.assertTrue(os.path.exists(d.name), 'TemporaryDirectory %s does not exist' % d.name)
        d.cleanup()
        TestTemporaryDirectory.assertFalse(os.path.exists(d.name), 'TemporaryDirectory %s exists after cleanup' % d.name)
    finally:
        os.rmdir(dir)

TestTemporaryDirectory = test_tempfile.TestTemporaryDirectory()
test_explicit_cleanup()
