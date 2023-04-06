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

def test_communicate_epipe_only_stdin():
    p = subprocess.Popen(test_subprocess.ZERO_RETURN_CMD, stdin=subprocess.PIPE)
    ProcessTestCase.addCleanup(p.stdin.close)
    p.wait()
    p.communicate(b'x' * 2 ** 20)

ProcessTestCase = test_subprocess.ProcessTestCase()
test_communicate_epipe_only_stdin()
