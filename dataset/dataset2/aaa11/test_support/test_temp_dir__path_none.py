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

def test_temp_dir__path_none():
    """Test passing no path."""
    with os_helper.temp_dir() as temp_path:
        TestSupport.assertTrue(os.path.isdir(temp_path))
    TestSupport.assertFalse(os.path.isdir(temp_path))

TestSupport = test_support.TestSupport()
test_temp_dir__path_none()
