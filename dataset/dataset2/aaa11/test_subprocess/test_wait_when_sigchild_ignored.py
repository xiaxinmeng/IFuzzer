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

def test_wait_when_sigchild_ignored():
    sigchild_ignore = support.findfile('sigchild_ignore.py', subdir='subprocessdata')
    p = subprocess.Popen([sys.executable, sigchild_ignore], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdout, stderr) = p.communicate()
    POSIXProcessTestCase.assertEqual(0, p.returncode, 'sigchild_ignore.py exited non-zero with this error:\n%s' % stderr.decode('utf-8'))

POSIXProcessTestCase = test_subprocess.POSIXProcessTestCase()
test_wait_when_sigchild_ignored()
