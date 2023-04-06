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

def test_stderr_with_capture_output_arg():
    tf = tempfile.TemporaryFile()
    RunFuncTestCase.addCleanup(tf.close)
    with RunFuncTestCase.assertRaises(ValueError, msg='Expected ValueError when stderr and capture_output args supplied.') as c:
        output = RunFuncTestCase.run_python("print('will not be run')", capture_output=True, stderr=tf)
    RunFuncTestCase.assertIn('stderr', c.exception.args[0])
    RunFuncTestCase.assertIn('capture_output', c.exception.args[0])

RunFuncTestCase = test_subprocess.RunFuncTestCase()
test_stderr_with_capture_output_arg()
