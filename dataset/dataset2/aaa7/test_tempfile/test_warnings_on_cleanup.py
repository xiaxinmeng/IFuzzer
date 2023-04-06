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

def test_warnings_on_cleanup():
    with TestTemporaryDirectory.do_create() as dir:
        d = TestTemporaryDirectory.do_create(dir=dir, recurse=3)
        name = d.name
        with warnings_helper.check_warnings(('Implicitly', ResourceWarning), quiet=False):
            warnings.filterwarnings('always', category=ResourceWarning)
            del d
            support.gc_collect()
        TestTemporaryDirectory.assertFalse(os.path.exists(name), 'TemporaryDirectory %s exists after __del__' % name)

TestTemporaryDirectory = test_tempfile.TestTemporaryDirectory()
test_warnings_on_cleanup()
