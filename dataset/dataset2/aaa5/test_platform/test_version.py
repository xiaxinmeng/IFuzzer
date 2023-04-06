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

def test_version():
    res = platform.version()

PlatformTest = test_platform.PlatformTest()
test_version()
