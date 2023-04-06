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

@unittest.skipIf(test_subprocess.mswindows, 'behavior currently not supported on Windows')
def test_file_not_found_with_bad_cwd():
    with ProcessTestCase.assertRaises(FileNotFoundError) as c:
        subprocess.Popen(['exit', '0'], cwd='/some/nonexistent/directory')
    ProcessTestCase.assertEqual(c.exception.filename, '/some/nonexistent/directory')

ProcessTestCase = test_subprocess.ProcessTestCase()
test_file_not_found_with_bad_cwd()
