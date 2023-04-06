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

def test_remove_partial():
    dira = os.path.join(os_helper.TESTFN, 'dira')
    os.mkdir(dira)
    dirb = os.path.join(dira, 'dirb')
    os.mkdir(dirb)
    create_file(os.path.join(dira, 'file.txt'))
    os.removedirs(dirb)
    RemoveDirsTests.assertFalse(os.path.exists(dirb))
    RemoveDirsTests.assertTrue(os.path.exists(dira))
    RemoveDirsTests.assertTrue(os.path.exists(os_helper.TESTFN))

RemoveDirsTests = test_os.RemoveDirsTests()
test_remove_partial()
