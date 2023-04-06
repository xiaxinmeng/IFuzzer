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

def test_writelines():
    f = TestSpooledTemporaryFile.do_create()
    f.writelines((b'x', b'y', b'z'))
    pos = f.seek(0)
    TestSpooledTemporaryFile.assertEqual(pos, 0)
    buf = f.read()
    TestSpooledTemporaryFile.assertEqual(buf, b'xyz')

TestSpooledTemporaryFile = test_tempfile.TestSpooledTemporaryFile()
test_writelines()
