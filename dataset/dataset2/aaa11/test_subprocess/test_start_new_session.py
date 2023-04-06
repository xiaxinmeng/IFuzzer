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

def test_start_new_session():
    try:
        output = subprocess.check_output([sys.executable, '-c', 'import os; print(os.getsid(0))'], start_new_session=True)
    except OSError as e:
        if e.errno != errno.EPERM:
            raise
    else:
        parent_sid = os.getsid(0)
        child_sid = int(output)
        POSIXProcessTestCase.assertNotEqual(parent_sid, child_sid)

POSIXProcessTestCase = test_subprocess.POSIXProcessTestCase()
test_start_new_session()
