import abc
import array
import errno
import locale
import os
import pickle
import random
import signal
import sys
import sysconfig
import textwrap
import threading
import time
import unittest
import warnings
import weakref
from collections import deque, UserList
from itertools import cycle, count
from test import support
from test.support.script_helper import assert_python_ok, assert_python_failure, run_python_until_end
from test.support import import_helper
from test.support import os_helper
from test.support import threading_helper
from test.support import warnings_helper
from test.support.os_helper import FakePath
import codecs
import io
import _pyio as pyio
import ctypes
import _testcapi
import test_io

@support.cpython_only
@unittest.skipIf(sys.flags.utf8_mode, 'utf-8 mode is enabled')
def test_device_encoding():
    import _testcapi
    b = TextIOWrapperTest.BytesIO()
    b.fileno = lambda : _testcapi.INT_MAX + 1
    TextIOWrapperTest.assertRaises(OverflowError, TextIOWrapperTest.TextIOWrapper, b)
    b.fileno = lambda : _testcapi.UINT_MAX + 1
    TextIOWrapperTest.assertRaises(OverflowError, TextIOWrapperTest.TextIOWrapper, b)

TextIOWrapperTest = test_io.TextIOWrapperTest()
test_device_encoding()
