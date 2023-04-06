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

@unittest.skipIf(test_subprocess.mswindows, "requires posix like 'sleep' shell command")
def test_run_with_shell_timeout_and_capture_output():
    """Output capturing after a timeout mustn't hang forever on open filehandles."""
    before_secs = time.monotonic()
    try:
        subprocess.run('sleep 3', shell=True, timeout=0.1, capture_output=True)
    except subprocess.TimeoutExpired as exc:
        after_secs = time.monotonic()
        stacks = traceback.format_exc()
    else:
        RunFuncTestCase.fail('TimeoutExpired not raised.')
    RunFuncTestCase.assertLess(after_secs - before_secs, 1.5, msg=f'TimeoutExpired was delayed! Bad traceback:\n```\n{stacks}```')

RunFuncTestCase = test_subprocess.RunFuncTestCase()
test_run_with_shell_timeout_and_capture_output()
