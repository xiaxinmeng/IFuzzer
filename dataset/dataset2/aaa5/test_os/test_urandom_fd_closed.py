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

def test_urandom_fd_closed():
    code = 'if 1:\n            import os\n            import sys\n            import test.support\n            os.urandom(4)\n            with test.support.SuppressCrashReport():\n                os.closerange(3, 256)\n            sys.stdout.buffer.write(os.urandom(4))\n            '
    (rc, out, err) = assert_python_ok('-Sc', code)

URandomFDTests = test_os.URandomFDTests()
test_urandom_fd_closed()
