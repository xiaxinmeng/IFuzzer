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

def test_preexec_exception():

    def raise_it():
        raise ValueError('What if two swallows carried a coconut?')
    try:
        p = subprocess.Popen([sys.executable, '-c', ''], preexec_fn=raise_it)
    except subprocess.SubprocessError as e:
        POSIXProcessTestCase.assertTrue(subprocess._posixsubprocess, 'Expected a ValueError from the preexec_fn')
    except ValueError as e:
        POSIXProcessTestCase.assertIn('coconut', e.args[0])
    else:
        POSIXProcessTestCase.fail('Exception raised by preexec_fn did not make it to the parent process.')

POSIXProcessTestCase = test_subprocess.POSIXProcessTestCase()
test_preexec_exception()
