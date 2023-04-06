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

def test_truncate_on_read_only():
    rawio = BufferedReaderTest.MockFileIO(b'abc')
    bufio = BufferedReaderTest.tp(rawio)
    BufferedReaderTest.assertFalse(bufio.writable())
    BufferedReaderTest.assertRaises(BufferedReaderTest.UnsupportedOperation, bufio.truncate)
    BufferedReaderTest.assertRaises(BufferedReaderTest.UnsupportedOperation, bufio.truncate, 0)

BufferedReaderTest = test_io.BufferedReaderTest()
test_truncate_on_read_only()
