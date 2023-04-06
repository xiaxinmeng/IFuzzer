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
has_textmode = (tempfile._text_openflags != tempfile._bin_openflags)
@unittest.skipUnless(has_textmode, 'text mode not available')
def test_textmode():
    f = TestMkstempInner.do_create(bin=0)
    f.write(b'blat\x1a')
    f.write(b'extra\n')
    os.lseek(f.fd, 0, os.SEEK_SET)
    TestMkstempInner.assertEqual(os.read(f.fd, 20), b'blat')

TestMkstempInner = test_tempfile.TestMkstempInner()
test_textmode()
