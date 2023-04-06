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

def test_has_no_name():
    dir = tempfile.mkdtemp()
    f = tempfile.TemporaryFile(dir=dir)
    f.write(b'blat')
    try:
        os.rmdir(dir)
    except:
        f.close()
        os.rmdir(dir)
        raise

TestTemporaryFile = test_tempfile.TestTemporaryFile()
test_has_no_name()
