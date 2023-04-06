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

def test_communicate_repeated_call_after_stdout_close():
    proc = subprocess.Popen([sys.executable, '-c', 'import os, time; os.close(1), time.sleep(2)'], stdout=subprocess.PIPE)
    while True:
        try:
            proc.communicate(timeout=0.1)
            return
        except subprocess.TimeoutExpired:
            pass

POSIXProcessTestCase = test_subprocess.POSIXProcessTestCase()
test_communicate_repeated_call_after_stdout_close()
