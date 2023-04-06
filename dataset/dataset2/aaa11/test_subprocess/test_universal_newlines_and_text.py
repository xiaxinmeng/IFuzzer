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

def test_universal_newlines_and_text():
    args = [sys.executable, '-c', 'import sys,os;' + test_subprocess.SETBINARY + 'buf = sys.stdout.buffer;buf.write(sys.stdin.readline().encode());buf.flush();buf.write(b"line2\\n");buf.flush();buf.write(sys.stdin.read().encode());buf.flush();buf.write(b"line4\\n");buf.flush();buf.write(b"line5\\r\\n");buf.flush();buf.write(b"line6\\r");buf.flush();buf.write(b"\\nline7");buf.flush();buf.write(b"\\nline8");']
    for extra_kwarg in ('universal_newlines', 'text'):
        p = subprocess.Popen(args, **{'stdin': subprocess.PIPE, 'stdout': subprocess.PIPE, extra_kwarg: True})
        with p:
            p.stdin.write('line1\n')
            p.stdin.flush()
            ProcessTestCase.assertEqual(p.stdout.readline(), 'line1\n')
            p.stdin.write('line3\n')
            p.stdin.close()
            ProcessTestCase.addCleanup(p.stdout.close)
            ProcessTestCase.assertEqual(p.stdout.readline(), 'line2\n')
            ProcessTestCase.assertEqual(p.stdout.read(6), 'line3\n')
            ProcessTestCase.assertEqual(p.stdout.read(), 'line4\nline5\nline6\nline7\nline8')

ProcessTestCase = test_subprocess.ProcessTestCase()
test_universal_newlines_and_text()
