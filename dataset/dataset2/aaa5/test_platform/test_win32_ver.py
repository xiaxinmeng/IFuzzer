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

def test_win32_ver():
    res = platform.win32_ver()

PlatformTest = test_platform.PlatformTest()
test_win32_ver()
