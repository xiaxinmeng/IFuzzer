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

def test_io_buffered_by_default():
    p = subprocess.Popen(test_subprocess.ZERO_RETURN_CMD, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        ProcessTestCase.assertIsInstance(p.stdin, io.BufferedIOBase)
        ProcessTestCase.assertIsInstance(p.stdout, io.BufferedIOBase)
        ProcessTestCase.assertIsInstance(p.stderr, io.BufferedIOBase)
    finally:
        p.stdin.close()
        p.stdout.close()
        p.stderr.close()
        p.wait()

ProcessTestCase = test_subprocess.ProcessTestCase()
test_io_buffered_by_default()
