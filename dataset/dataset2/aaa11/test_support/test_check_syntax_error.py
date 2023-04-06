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

def test_check_syntax_error():
    support.check_syntax_error(TestSupport, 'def class', lineno=1, offset=5)
    with TestSupport.assertRaises(AssertionError):
        support.check_syntax_error(TestSupport, 'x=1')

TestSupport = test_support.TestSupport()
test_check_syntax_error()
