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

def test_temp_cwd__name_none():
    """Test passing None to temp_cwd()."""
    original_cwd = os.getcwd()
    with os_helper.temp_cwd(name=None) as new_cwd:
        TestSupport.assertNotEqual(new_cwd, original_cwd)
        TestSupport.assertTrue(os.path.isdir(new_cwd))
        TestSupport.assertEqual(os.getcwd(), new_cwd)
    TestSupport.assertEqual(os.getcwd(), original_cwd)

TestSupport = test_support.TestSupport()
test_temp_cwd__name_none()
