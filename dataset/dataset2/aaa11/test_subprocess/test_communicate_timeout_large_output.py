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

def test_communicate_timeout_large_output():
    p = subprocess.Popen([sys.executable, '-c', 'import sys,os,time;sys.stdout.write("a" * (64 * 1024));time.sleep(0.2);sys.stdout.write("a" * (64 * 1024));time.sleep(0.2);sys.stdout.write("a" * (64 * 1024));time.sleep(0.2);sys.stdout.write("a" * (64 * 1024));'], stdout=subprocess.PIPE)
    ProcessTestCase.assertRaises(subprocess.TimeoutExpired, p.communicate, timeout=0.4)
    (stdout, _) = p.communicate()
    ProcessTestCase.assertEqual(len(stdout), 4 * 64 * 1024)

ProcessTestCase = test_subprocess.ProcessTestCase()
test_communicate_timeout_large_output()
