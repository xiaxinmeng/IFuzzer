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

def test_write_non_blocking():
    raw = BufferedWriterTest.MockNonBlockWriterIO()
    bufio = BufferedWriterTest.tp(raw, 8)
    BufferedWriterTest.assertEqual(bufio.write(b'abcd'), 4)
    BufferedWriterTest.assertEqual(bufio.write(b'efghi'), 5)
    raw.block_on(b'k')
    BufferedWriterTest.assertEqual(bufio.write(b'jklmn'), 5)
    raw.block_on(b'0')
    try:
        bufio.write(b'opqrwxyz0123456789')
    except BufferedWriterTest.BlockingIOError as e:
        written = e.characters_written
    else:
        BufferedWriterTest.fail('BlockingIOError should have been raised')
    BufferedWriterTest.assertEqual(written, 16)
    BufferedWriterTest.assertEqual(raw.pop_written(), b'abcdefghijklmnopqrwxyz')
    BufferedWriterTest.assertEqual(bufio.write(b'ABCDEFGHI'), 9)
    s = raw.pop_written()
    BufferedWriterTest.assertTrue(s.startswith(b'01234567A'), s)

BufferedWriterTest = test_io.BufferedWriterTest()
test_write_non_blocking()
