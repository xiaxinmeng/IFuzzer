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

def test_large_file_ops():
    if sys.platform[:3] == 'win' or sys.platform == 'darwin':
        support.requires('largefile', 'test requires %s bytes and a long time to run' % IOTest.LARGE)
    with IOTest.open(os_helper.TESTFN, 'w+b', 0) as f:
        IOTest.large_file_ops(f)
    with IOTest.open(os_helper.TESTFN, 'w+b') as f:
        IOTest.large_file_ops(f)

IOTest = test_io.IOTest()
test_large_file_ops()
