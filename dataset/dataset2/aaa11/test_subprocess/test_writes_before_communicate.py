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

def test_writes_before_communicate():
    p = subprocess.Popen([sys.executable, '-c', 'import sys,os;sys.stdout.write(sys.stdin.read())'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ProcessTestCase.addCleanup(p.stdout.close)
    ProcessTestCase.addCleanup(p.stderr.close)
    ProcessTestCase.addCleanup(p.stdin.close)
    p.stdin.write(b'banana')
    (stdout, stderr) = p.communicate(b'split')
    ProcessTestCase.assertEqual(stdout, b'bananasplit')
    ProcessTestCase.assertEqual(stderr, b'')

ProcessTestCase = test_subprocess.ProcessTestCase()
test_writes_before_communicate()
