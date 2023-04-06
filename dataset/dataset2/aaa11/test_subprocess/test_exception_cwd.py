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

def test_exception_cwd():
    """Test error in the child raised in the parent for a bad cwd."""
    desired_exception = POSIXProcessTestCase._get_chdir_exception()
    try:
        p = subprocess.Popen([sys.executable, '-c', ''], cwd=POSIXProcessTestCase._nonexistent_dir)
    except OSError as e:
        POSIXProcessTestCase.assertEqual(desired_exception.errno, e.errno)
        POSIXProcessTestCase.assertEqual(desired_exception.strerror, e.strerror)
        POSIXProcessTestCase.assertEqual(desired_exception.filename, e.filename)
    else:
        POSIXProcessTestCase.fail('Expected OSError: %s' % desired_exception)

POSIXProcessTestCase = test_subprocess.POSIXProcessTestCase()
POSIXProcessTestCase.setUp()
test_exception_cwd()
