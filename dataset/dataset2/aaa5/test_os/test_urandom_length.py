import asynchat
import asyncore
import codecs
import contextlib
import decimal
import errno
import fnmatch
import fractions
import itertools
import locale
import mmap
import os
import pickle
import select
import shutil
import signal
import socket
import stat
import struct
import subprocess
import sys
import sysconfig
import tempfile
import threading
import time
import types
import unittest
import uuid
import warnings
from test import support
from test.support import import_helper
from test.support import os_helper
from test.support import socket_helper
from test.support import threading_helper
from test.support import warnings_helper
from platform import win32_is_iot
import resource
import fcntl

import pwd
from _testcapi import INT_MAX, PY_SSIZE_T_MAX
from test.support.script_helper import assert_python_ok
from test.support import unix_shell
from test.support.os_helper import FakePath
import ctypes
from test import mapping_tests
import ctypes
from ctypes import wintypes

from ctypes import wintypes
import ctypes
import ctypes.wintypes
import pickle
import pickle
import test_os

def test_urandom_length():
    URandomTests.assertEqual(len(os.urandom(0)), 0)
    URandomTests.assertEqual(len(os.urandom(1)), 1)
    URandomTests.assertEqual(len(os.urandom(10)), 10)
    URandomTests.assertEqual(len(os.urandom(100)), 100)
    URandomTests.assertEqual(len(os.urandom(1000)), 1000)

URandomTests = test_os.URandomTests()
test_urandom_length()
