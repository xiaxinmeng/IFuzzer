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

def test_python_is_optimized():
    TestSupport.assertIsInstance(support.python_is_optimized(), bool)

TestSupport = test_support.TestSupport()
test_python_is_optimized()
