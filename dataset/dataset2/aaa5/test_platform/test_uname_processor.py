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

@unittest.skipIf(sys.platform in ['win32', 'OpenVMS'], 'uname -p not used')
def test_uname_processor():
    """
        On some systems, the processor must match the output
        of 'uname -p'. See Issue 35967 for rationale.
        """
    try:
        proc_res = subprocess.check_output(['uname', '-p'], text=True).strip()
        expect = platform._unknown_as_blank(proc_res)
    except (OSError, subprocess.CalledProcessError):
        expect = ''
    PlatformTest.assertEqual(platform.uname().processor, expect)

PlatformTest = test_platform.PlatformTest()
test_uname_processor()
