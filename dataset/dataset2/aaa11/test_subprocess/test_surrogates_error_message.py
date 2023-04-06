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

def test_surrogates_error_message():

    def prepare():
        raise ValueError('surrogate:\udcff')
    try:
        subprocess.call(test_subprocess.ZERO_RETURN_CMD, preexec_fn=prepare)
    except ValueError as err:
        POSIXProcessTestCase.assertIsNone(subprocess._posixsubprocess)
        POSIXProcessTestCase.assertEqual(str(err), 'surrogate:\udcff')
    except subprocess.SubprocessError as err:
        POSIXProcessTestCase.assertIsNotNone(subprocess._posixsubprocess)
        POSIXProcessTestCase.assertEqual(str(err), 'Exception occurred in preexec_fn.')
    else:
        POSIXProcessTestCase.fail('Expected ValueError or subprocess.SubprocessError')

POSIXProcessTestCase = test_subprocess.POSIXProcessTestCase()
test_surrogates_error_message()
