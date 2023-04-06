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

def test_check_output_stdin_with_input_arg():
    tf = tempfile.TemporaryFile()
    ProcessTestCase.addCleanup(tf.close)
    tf.write(b'pear')
    tf.seek(0)
    with ProcessTestCase.assertRaises(ValueError, msg='Expected ValueError when stdin and input args supplied.') as c:
        output = ProcessTestCase.run_python("print('will not be run')", stdin=tf, input=b'hare')
    ProcessTestCase.assertIn('stdin', c.exception.args[0])
    ProcessTestCase.assertIn('input', c.exception.args[0])

ProcessTestCase = test_subprocess.ProcessTestCase()
test_check_output_stdin_with_input_arg()
