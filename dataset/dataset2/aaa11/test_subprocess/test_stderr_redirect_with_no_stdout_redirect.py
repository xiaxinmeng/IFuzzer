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

def test_stderr_redirect_with_no_stdout_redirect():
    p = subprocess.Popen([sys.executable, '-c', 'import sys, subprocess;rc = subprocess.call([sys.executable, "-c",    "import sys;"    "sys.stderr.write(\'42\')"],    stderr=subprocess.STDOUT);sys.exit(rc)'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdout, stderr) = p.communicate()
    ProcessTestCase.assertEqual(stdout, b'42')
    ProcessTestCase.assertEqual(stderr, b'')
    ProcessTestCase.assertEqual(p.returncode, 0)

ProcessTestCase = test_subprocess.ProcessTestCase()
test_stderr_redirect_with_no_stdout_redirect()
