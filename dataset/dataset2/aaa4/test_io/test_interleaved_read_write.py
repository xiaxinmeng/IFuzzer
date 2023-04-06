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

def test_interleaved_read_write():
    with BufferedRandomTest.BytesIO(b'abcdefgh') as raw:
        with BufferedRandomTest.tp(raw, 100) as f:
            f.write(b'1')
            BufferedRandomTest.assertEqual(f.read(1), b'b')
            f.write(b'2')
            BufferedRandomTest.assertEqual(f.read1(1), b'd')
            f.write(b'3')
            buf = bytearray(1)
            f.readinto(buf)
            BufferedRandomTest.assertEqual(buf, b'f')
            f.write(b'4')
            BufferedRandomTest.assertEqual(f.peek(1), b'h')
            f.flush()
            BufferedRandomTest.assertEqual(raw.getvalue(), b'1b2d3f4h')
    with BufferedRandomTest.BytesIO(b'abc') as raw:
        with BufferedRandomTest.tp(raw, 100) as f:
            BufferedRandomTest.assertEqual(f.read(1), b'a')
            f.write(b'2')
            BufferedRandomTest.assertEqual(f.read(1), b'c')
            f.flush()
            BufferedRandomTest.assertEqual(raw.getvalue(), b'a2c')

BufferedRandomTest = test_io.BufferedRandomTest()
test_interleaved_read_write()
