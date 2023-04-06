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

@unittest.skipUnless(os.path.isdir('/proc/%d/fd' % os.getpid()), 'Linux specific')
def test_failed_child_execute_fd_leak():
    """Test for the fork() failure fd leak reported in issue16327."""
    fd_directory = '/proc/%d/fd' % os.getpid()
    fds_before_popen = os.listdir(fd_directory)
    with ProcessTestCase.assertRaises(test_subprocess.PopenTestException):
        test_subprocess.PopenExecuteChildRaises(test_subprocess.ZERO_RETURN_CMD, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    fds_after_exception = os.listdir(fd_directory)
    ProcessTestCase.assertEqual(fds_before_popen, fds_after_exception)

ProcessTestCase = test_subprocess.ProcessTestCase()
test_failed_child_execute_fd_leak()
