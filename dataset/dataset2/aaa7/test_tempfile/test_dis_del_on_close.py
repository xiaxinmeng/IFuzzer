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

def test_dis_del_on_close():
    dir = tempfile.mkdtemp()
    tmp = None
    try:
        f = tempfile.NamedTemporaryFile(dir=dir, delete=False)
        tmp = f.name
        f.write(b'blat')
        f.close()
        TestNamedTemporaryFile.assertTrue(os.path.exists(f.name), 'NamedTemporaryFile %s missing after close' % f.name)
    finally:
        if tmp is not None:
            os.unlink(tmp)
        os.rmdir(dir)

TestNamedTemporaryFile = test_tempfile.TestNamedTemporaryFile()
test_dis_del_on_close()
