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

def test_DirsOnSysPath():
    with import_helper.DirsOnSysPath('foo', 'bar'):
        TestSupport.assertIn('foo', sys.path)
        TestSupport.assertIn('bar', sys.path)
    TestSupport.assertNotIn('foo', sys.path)
    TestSupport.assertNotIn('bar', sys.path)

TestSupport = test_support.TestSupport()
test_DirsOnSysPath()
