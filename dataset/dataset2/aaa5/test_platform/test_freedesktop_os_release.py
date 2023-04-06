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

def test_freedesktop_os_release():
    PlatformTest.addCleanup(PlatformTest.clear_caches)
    PlatformTest.clear_caches()
    if any((os.path.isfile(fn) for fn in platform._os_release_candidates)):
        info = platform.freedesktop_os_release()
        PlatformTest.assertIn('NAME', info)
        PlatformTest.assertIn('ID', info)
        info['CPYTHON_TEST'] = 'test'
        PlatformTest.assertNotIn('CPYTHON_TEST', platform.freedesktop_os_release())
    else:
        with PlatformTest.assertRaises(OSError):
            platform.freedesktop_os_release()

PlatformTest = test_platform.PlatformTest()
test_freedesktop_os_release()
