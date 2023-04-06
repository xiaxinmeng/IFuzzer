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

def test_select_unbuffered():
    select = import_helper.import_module('select')
    p = subprocess.Popen([sys.executable, '-c', 'import sys;sys.stdout.write("apple")'], stdout=subprocess.PIPE, bufsize=0)
    f = p.stdout
    POSIXProcessTestCase.addCleanup(f.close)
    try:
        POSIXProcessTestCase.assertEqual(f.read(4), b'appl')
        POSIXProcessTestCase.assertIn(f, select.select([f], [], [], 0.0)[0])
    finally:
        p.wait()

POSIXProcessTestCase = test_subprocess.POSIXProcessTestCase()
test_select_unbuffered()
