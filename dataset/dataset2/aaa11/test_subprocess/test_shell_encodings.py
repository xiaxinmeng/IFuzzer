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

def test_shell_encodings():
    for enc in ['ansi', 'oem']:
        newenv = os.environ.copy()
        newenv['FRUIT'] = 'physalis'
        p = subprocess.Popen('set', shell=1, stdout=subprocess.PIPE, env=newenv, encoding=enc)
        with p:
            Win32ProcessTestCase.assertIn('physalis', p.stdout.read(), enc)

Win32ProcessTestCase = test_subprocess.Win32ProcessTestCase()
test_shell_encodings()
