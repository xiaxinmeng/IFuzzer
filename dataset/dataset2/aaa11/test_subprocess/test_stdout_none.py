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

def test_stdout_none():
    code = 'import sys; from subprocess import Popen, PIPE;p = Popen([sys.executable, "-c", "print(\'test_stdout_none\')"],          stdin=PIPE, stderr=PIPE);p.wait(); assert p.stdout is None;'
    p = subprocess.Popen([sys.executable, '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ProcessTestCase.addCleanup(p.stdout.close)
    ProcessTestCase.addCleanup(p.stderr.close)
    (out, err) = p.communicate()
    ProcessTestCase.assertEqual(p.returncode, 0, err)
    ProcessTestCase.assertEqual(out.rstrip(), b'test_stdout_none')

ProcessTestCase = test_subprocess.ProcessTestCase()
test_stdout_none()
