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

def test_list2cmdline():
    ProcessTestCase.assertEqual(subprocess.list2cmdline(['a b c', 'd', 'e']), '"a b c" d e')
    ProcessTestCase.assertEqual(subprocess.list2cmdline(['ab"c', '\\', 'd']), 'ab\\"c \\ d')
    ProcessTestCase.assertEqual(subprocess.list2cmdline(['ab"c', ' \\', 'd']), 'ab\\"c " \\\\" d')
    ProcessTestCase.assertEqual(subprocess.list2cmdline(['a\\\\\\b', 'de fg', 'h']), 'a\\\\\\b "de fg" h')
    ProcessTestCase.assertEqual(subprocess.list2cmdline(['a\\"b', 'c', 'd']), 'a\\\\\\"b c d')
    ProcessTestCase.assertEqual(subprocess.list2cmdline(['a\\\\b c', 'd', 'e']), '"a\\\\b c" d e')
    ProcessTestCase.assertEqual(subprocess.list2cmdline(['a\\\\b\\ c', 'd', 'e']), '"a\\\\b\\ c" d e')
    ProcessTestCase.assertEqual(subprocess.list2cmdline(['ab', '']), 'ab ""')

ProcessTestCase = test_subprocess.ProcessTestCase()
test_list2cmdline()
