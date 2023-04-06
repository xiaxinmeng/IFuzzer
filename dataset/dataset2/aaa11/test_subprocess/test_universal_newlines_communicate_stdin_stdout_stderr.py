import unittest
from unittest import mock
from test import support
from test.support import import_helper
from test.support import os_helper
from test.support import warnings_helper
import subprocess
import sys
import signal
import io
import itertools
import os
import errno
import tempfile
import time
import traceback
import types
import selectors
import sysconfig
import select
import shutil
import threading
import gc
import textwrap
import json
from test.support.os_helper import FakePath
import _testcapi
import pwd
import grp
import fcntl

from resource import getrlimit, setrlimit, RLIMIT_NPROC
import _posixsubprocess

import types
import test_subprocess

def test_universal_newlines_communicate_stdin_stdout_stderr():
    p = subprocess.Popen([sys.executable, '-c', 'import sys,os;' + test_subprocess.SETBINARY + textwrap.dedent('\n                               s = sys.stdin.buffer.readline()\n                               sys.stdout.buffer.write(s)\n                               sys.stdout.buffer.write(b"line2\\r")\n                               sys.stderr.buffer.write(b"eline2\\n")\n                               s = sys.stdin.buffer.read()\n                               sys.stdout.buffer.write(s)\n                               sys.stdout.buffer.write(b"line4\\n")\n                               sys.stdout.buffer.write(b"line5\\r\\n")\n                               sys.stderr.buffer.write(b"eline6\\r")\n                               sys.stderr.buffer.write(b"eline7\\r\\nz")\n                              ')], stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    ProcessTestCase.addCleanup(p.stdout.close)
    ProcessTestCase.addCleanup(p.stderr.close)
    (stdout, stderr) = p.communicate('line1\nline3\n')
    ProcessTestCase.assertEqual(p.returncode, 0)
    ProcessTestCase.assertEqual('line1\nline2\nline3\nline4\nline5\n', stdout)
    ProcessTestCase.assertTrue(stderr.startswith('eline2\neline6\neline7\n'))

ProcessTestCase = test_subprocess.ProcessTestCase()
test_universal_newlines_communicate_stdin_stdout_stderr()
