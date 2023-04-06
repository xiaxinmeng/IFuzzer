import errno
import importlib
import io
import os
import shutil
import socket
import stat
import subprocess
import sys
import tempfile
import textwrap
import time
import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
from test.support import script_helper
from test.support import socket_helper
from test.support import warnings_helper
import sched
import importlib
import test_support

def test_args_from_interpreter_flags():
    for opts in ([], ['-B'], ['-s'], ['-S'], ['-E'], ['-v'], ['-b'], ['-q'], ['-I'], ['-bb'], ['-vvv'], ['-Wignore'], ['-X', 'dev'], ['-Wignore', '-X', 'dev'], ['-X', 'faulthandler'], ['-X', 'importtime'], ['-X', 'showrefcount'], ['-X', 'tracemalloc'], ['-X', 'tracemalloc=3']):
        with TestSupport.subTest(opts=opts):
            TestSupport.check_options(opts, 'args_from_interpreter_flags')
    TestSupport.check_options(['-I', '-E', '-s'], 'args_from_interpreter_flags', ['-I'])

TestSupport = test_support.TestSupport()
test_args_from_interpreter_flags()
