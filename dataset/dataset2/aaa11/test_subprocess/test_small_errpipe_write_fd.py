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

def test_small_errpipe_write_fd():
    """Issue #15798: Popen should work when stdio fds are available."""
    new_stdin = os.dup(0)
    new_stdout = os.dup(1)
    try:
        os.close(0)
        os.close(1)
        subprocess.Popen([sys.executable, '-c', "print('AssertionError:0:CLOEXEC failure.')"]).wait()
    finally:
        os.dup2(new_stdin, 0)
        os.dup2(new_stdout, 1)
        os.close(new_stdin)
        os.close(new_stdout)

POSIXProcessTestCase = test_subprocess.POSIXProcessTestCase()
test_small_errpipe_write_fd()
