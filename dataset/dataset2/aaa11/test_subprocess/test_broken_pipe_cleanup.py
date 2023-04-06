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

def test_broken_pipe_cleanup():
    """Broken pipe error should not prevent wait() (Issue 21619)"""
    proc = subprocess.Popen(test_subprocess.ZERO_RETURN_CMD, stdin=subprocess.PIPE, bufsize=support.PIPE_MAX_SIZE * 2)
    proc = proc.__enter__()
    proc.stdin.write(b'x' * support.PIPE_MAX_SIZE)
    ContextManagerTests.assertIsNone(proc.returncode)
    ContextManagerTests.assertRaises(OSError, proc.__exit__, None, None, None)
    ContextManagerTests.assertEqual(proc.returncode, 0)
    ContextManagerTests.assertTrue(proc.stdin.closed)

ContextManagerTests = test_subprocess.ContextManagerTests()
test_broken_pipe_cleanup()
