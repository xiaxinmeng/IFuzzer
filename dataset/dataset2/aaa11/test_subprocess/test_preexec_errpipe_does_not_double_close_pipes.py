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

@unittest.skipIf(not os.path.exists('/dev/zero'), '/dev/zero required.')
def test_preexec_errpipe_does_not_double_close_pipes():
    """Issue16140: Don't double close pipes on preexec error."""

    def raise_it():
        raise subprocess.SubprocessError('force the _execute_child() errpipe_data path.')
    with POSIXProcessTestCase.assertRaises(subprocess.SubprocessError):
        POSIXProcessTestCase._TestExecuteChildPopen(POSIXProcessTestCase, test_subprocess.ZERO_RETURN_CMD, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=raise_it)

POSIXProcessTestCase = test_subprocess.POSIXProcessTestCase()
test_preexec_errpipe_does_not_double_close_pipes()
