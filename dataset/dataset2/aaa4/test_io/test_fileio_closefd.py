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

def test_fileio_closefd():
    with IOTest.open(__file__, 'rb') as f1, IOTest.open(__file__, 'rb') as f2:
        fileio = IOTest.FileIO(f1.fileno(), closefd=False)
        fileio.__init__(f2.fileno(), closefd=False)
        f1.readline()
        fileio.close()
        f2.readline()

IOTest = test_io.IOTest()
test_fileio_closefd()
