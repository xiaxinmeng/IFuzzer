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

def test_read_non_blocking():
    rawio = BufferedReaderTest.MockRawIO((b'abc', b'd', None, b'efg', None, None, None))
    bufio = BufferedReaderTest.tp(rawio)
    BufferedReaderTest.assertEqual(b'abcd', bufio.read(6))
    BufferedReaderTest.assertEqual(b'e', bufio.read(1))
    BufferedReaderTest.assertEqual(b'fg', bufio.read())
    BufferedReaderTest.assertEqual(b'', bufio.peek(1))
    BufferedReaderTest.assertIsNone(bufio.read())
    BufferedReaderTest.assertEqual(b'', bufio.read())
    rawio = BufferedReaderTest.MockRawIO((b'a', None, None))
    BufferedReaderTest.assertEqual(b'a', rawio.readall())
    BufferedReaderTest.assertIsNone(rawio.readall())

BufferedReaderTest = test_io.BufferedReaderTest()
test_read_non_blocking()
