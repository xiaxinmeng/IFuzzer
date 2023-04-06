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

def test_universal_newlines_communicate():
    p = subprocess.Popen([sys.executable, '-c', 'import sys,os;' + test_subprocess.SETBINARY + 'buf = sys.stdout.buffer;buf.write(b"line2\\n");buf.flush();buf.write(b"line4\\n");buf.flush();buf.write(b"line5\\r\\n");buf.flush();buf.write(b"line6\\r");buf.flush();buf.write(b"\\nline7");buf.flush();buf.write(b"\\nline8");'], stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=1)
    ProcessTestCase.addCleanup(p.stdout.close)
    ProcessTestCase.addCleanup(p.stderr.close)
    (stdout, stderr) = p.communicate()
    ProcessTestCase.assertEqual(stdout, 'line2\nline4\nline5\nline6\nline7\nline8')

ProcessTestCase = test_subprocess.ProcessTestCase()
test_universal_newlines_communicate()
