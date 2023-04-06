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
TESTFN = os_helper.TESTFN
def test_temp_cwd():
    here = os.getcwd()
    with os_helper.temp_cwd(name=TESTFN):
        TestSupport.assertEqual(os.path.basename(os.getcwd()), TESTFN)
    TestSupport.assertFalse(os.path.exists(TESTFN))
    TestSupport.assertEqual(os.getcwd(), here)

TestSupport = test_support.TestSupport()
test_temp_cwd()
