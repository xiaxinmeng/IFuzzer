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

def test_communicate_timeout():
    p = subprocess.Popen([sys.executable, '-c', 'import sys,os,time;sys.stderr.write("pineapple\\n");time.sleep(1);sys.stderr.write("pear\\n");sys.stdout.write(sys.stdin.read())'], universal_newlines=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ProcessTestCase.assertRaises(subprocess.TimeoutExpired, p.communicate, 'banana', timeout=0.3)
    (stdout, stderr) = p.communicate()
    ProcessTestCase.assertEqual(stdout, 'banana')
    ProcessTestCase.assertEqual(stderr.encode(), b'pineapple\npear\n')

ProcessTestCase = test_subprocess.ProcessTestCase()
test_communicate_timeout()
