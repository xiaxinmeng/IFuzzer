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

def test_make_bad_fd():
    fd = os_helper.make_bad_fd()
    with TestSupport.assertRaises(OSError) as cm:
        os.write(fd, b'foo')
    TestSupport.assertEqual(cm.exception.errno, errno.EBADF)

TestSupport = test_support.TestSupport()
test_make_bad_fd()
