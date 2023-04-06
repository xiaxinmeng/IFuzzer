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

@support.cpython_only
def test_del_on_collection():
    dir = tempfile.mkdtemp()
    try:
        d = TestTemporaryDirectory.do_create(dir=dir)
        name = d.name
        del d
        TestTemporaryDirectory.assertFalse(os.path.exists(name), 'TemporaryDirectory %s exists after __del__' % name)
    finally:
        os.rmdir(dir)

TestTemporaryDirectory = test_tempfile.TestTemporaryDirectory()
test_del_on_collection()
