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

def test_detect_api_mismatch():
    missing_items = support.detect_api_mismatch(TestSupport.RefClass, TestSupport.OtherClass)
    TestSupport.assertEqual({'attribute1'}, missing_items)
    missing_items = support.detect_api_mismatch(TestSupport.OtherClass, TestSupport.RefClass)
    TestSupport.assertEqual({'attribute3', '__magic_2__'}, missing_items)

TestSupport = test_support.TestSupport()
test_detect_api_mismatch()
