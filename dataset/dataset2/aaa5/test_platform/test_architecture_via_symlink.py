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

@os_helper.skip_unless_symlink
def test_architecture_via_symlink():
    with support.PythonSymlink() as py:
        cmd = ('-c', 'import platform; print(platform.architecture())')
        PlatformTest.assertEqual(py.call_real(*cmd), py.call_link(*cmd))

PlatformTest = test_platform.PlatformTest()
test_architecture_via_symlink()
