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

def test_multiple_close():
    d = TestNamedTemporaryFile.do_create()
    d.cleanup()
    d.cleanup()
    d.cleanup()

TestNamedTemporaryFile = test_tempfile.TestNamedTemporaryFile()
TestNamedTemporaryFile.setUp()
test_multiple_close()
