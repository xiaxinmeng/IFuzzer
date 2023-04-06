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

def test_change_cwd():
    original_cwd = os.getcwd()
    with os_helper.temp_dir() as temp_path:
        with os_helper.change_cwd(temp_path) as new_cwd:
            TestSupport.assertEqual(new_cwd, temp_path)
            TestSupport.assertEqual(os.getcwd(), new_cwd)
    TestSupport.assertEqual(os.getcwd(), original_cwd)

TestSupport = test_support.TestSupport()
test_change_cwd()
