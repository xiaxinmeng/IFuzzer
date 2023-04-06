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

def test_java_ver():
    res = platform.java_ver()
    if sys.platform == 'java':
        PlatformTest.assertTrue(all(res))

PlatformTest = test_platform.PlatformTest()
test_java_ver()
