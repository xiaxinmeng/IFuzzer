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

def test_system_alias():
    res = platform.system_alias(platform.system(), platform.release(), platform.version())

PlatformTest = test_platform.PlatformTest()
test_system_alias()
