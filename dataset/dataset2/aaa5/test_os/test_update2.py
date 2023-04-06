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

@unittest.skipUnless(unix_shell and os.path.exists(unix_shell), 'requires a shell')
@unittest.skipUnless(hasattr(os, 'popen'), 'needs os.popen()')
def test_update2():
    os.environ.clear()
    os.environ.update(HELLO='World')
    with os.popen("%s -c 'echo $HELLO'" % unix_shell) as popen:
        value = popen.read().strip()
        EnvironTests.assertEqual(value, 'World')

EnvironTests = test_os.EnvironTests()
test_update2()
