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

def test_stderr_devnull():
    p = subprocess.Popen([sys.executable, '-c', 'import sys\nfor i in range(10240):sys.stderr.write("x" * 1024)'], stderr=subprocess.DEVNULL)
    p.wait()
    ProcessTestCase.assertEqual(p.stderr, None)

ProcessTestCase = test_subprocess.ProcessTestCase()
test_stderr_devnull()
