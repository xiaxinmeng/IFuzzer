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

def test_check_output_timeout():
    with ProcessTestCase.assertRaises(subprocess.TimeoutExpired) as c:
        cp = ProcessTestCase.run_python("import sys, time\nsys.stdout.write('BDFL')\nsys.stdout.flush()\ntime.sleep(3600)", timeout=3, stdout=subprocess.PIPE)
    ProcessTestCase.assertEqual(c.exception.output, b'BDFL')
    ProcessTestCase.assertEqual(c.exception.stdout, b'BDFL')

ProcessTestCase = test_subprocess.ProcessTestCase()
test_check_output_timeout()
