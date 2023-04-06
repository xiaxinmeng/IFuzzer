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

def test_send_signal_race():
    proc = subprocess.Popen(test_subprocess.ZERO_RETURN_CMD)
    support.wait_process(proc.pid, exitcode=0)
    POSIXProcessTestCase.assertIsNone(proc.returncode)
    with mock.patch('os.kill') as mock_kill:
        proc.send_signal(signal.SIGTERM)
    mock_kill.assert_not_called()
    POSIXProcessTestCase.assertIsNotNone(proc.returncode)

POSIXProcessTestCase = test_subprocess.POSIXProcessTestCase()
test_send_signal_race()