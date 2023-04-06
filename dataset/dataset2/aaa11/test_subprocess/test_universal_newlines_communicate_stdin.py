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

def test_universal_newlines_communicate_stdin():
    p = subprocess.Popen([sys.executable, '-c', 'import sys,os;' + test_subprocess.SETBINARY + textwrap.dedent('\n                               s = sys.stdin.readline()\n                               assert s == "line1\\n", repr(s)\n                               s = sys.stdin.read()\n                               assert s == "line3\\n", repr(s)\n                              ')], stdin=subprocess.PIPE, universal_newlines=1)
    (stdout, stderr) = p.communicate('line1\nline3\n')
    ProcessTestCase.assertEqual(p.returncode, 0)

ProcessTestCase = test_subprocess.ProcessTestCase()
test_universal_newlines_communicate_stdin()
