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

def test_io_unbuffered_works():
    p = subprocess.Popen(test_subprocess.ZERO_RETURN_CMD, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=0)
    try:
        ProcessTestCase.assertIsInstance(p.stdin, io.RawIOBase)
        ProcessTestCase.assertIsInstance(p.stdout, io.RawIOBase)
        ProcessTestCase.assertIsInstance(p.stderr, io.RawIOBase)
    finally:
        p.stdin.close()
        p.stdout.close()
        p.stderr.close()
        p.wait()

ProcessTestCase = test_subprocess.ProcessTestCase()
test_io_unbuffered_works()
