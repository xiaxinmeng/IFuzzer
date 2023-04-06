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

def test_wait_timeout():
    p = subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(0.3)'])
    with ProcessTestCase.assertRaises(subprocess.TimeoutExpired) as c:
        p.wait(timeout=0.0001)
    ProcessTestCase.assertIn('0.0001', str(c.exception))
    ProcessTestCase.assertEqual(p.wait(timeout=support.SHORT_TIMEOUT), 0)

ProcessTestCase = test_subprocess.ProcessTestCase()
test_wait_timeout()
