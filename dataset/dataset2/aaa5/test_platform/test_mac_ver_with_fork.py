import os
import platform
import subprocess
import sys
import unittest
from unittest import mock
from test import support
from test.support import os_helper

from platform import _comparable_version as V
import test_platform

@unittest.skipUnless(sys.platform == 'darwin', 'OSX only test')
def test_mac_ver_with_fork():
    pid = os.fork()
    if pid == 0:
        info = platform.mac_ver()
        os._exit(0)
    else:
        support.wait_process(pid, exitcode=0)

PlatformTest = test_platform.PlatformTest()
test_mac_ver_with_fork()
