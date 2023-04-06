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

def test_swap_fds():
    POSIXProcessTestCase.check_swap_fds(0, 1, 2)
    POSIXProcessTestCase.check_swap_fds(0, 2, 1)
    POSIXProcessTestCase.check_swap_fds(1, 0, 2)
    POSIXProcessTestCase.check_swap_fds(1, 2, 0)
    POSIXProcessTestCase.check_swap_fds(2, 0, 1)
    POSIXProcessTestCase.check_swap_fds(2, 1, 0)

POSIXProcessTestCase = test_subprocess.POSIXProcessTestCase()
test_swap_fds()
