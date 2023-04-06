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

def test_uname_cast_to_tuple():
    res = platform.uname()
    expected = (res.system, res.node, res.release, res.version, res.machine, res.processor)
    PlatformTest.assertEqual(tuple(res), expected)

PlatformTest = test_platform.PlatformTest()
test_uname_cast_to_tuple()
