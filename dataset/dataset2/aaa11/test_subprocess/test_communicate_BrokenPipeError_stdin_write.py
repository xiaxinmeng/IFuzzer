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

def test_communicate_BrokenPipeError_stdin_write():
    proc = subprocess.Popen(test_subprocess.ZERO_RETURN_CMD)
    with proc, mock.patch.object(proc, 'stdin') as mock_proc_stdin:
        mock_proc_stdin.write.side_effect = BrokenPipeError
        proc.communicate(b'stuff')
        mock_proc_stdin.write.assert_called_once_with(b'stuff')
        mock_proc_stdin.close.assert_called_once_with()

POSIXProcessTestCase = test_subprocess.POSIXProcessTestCase()
test_communicate_BrokenPipeError_stdin_write()
