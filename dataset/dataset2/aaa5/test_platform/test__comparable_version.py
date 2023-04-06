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

@support.cpython_only
def test__comparable_version():
    from platform import _comparable_version as V
    PlatformTest.assertEqual(V('1.2.3'), V('1.2.3'))
    PlatformTest.assertLess(V('1.2.3'), V('1.2.10'))
    PlatformTest.assertEqual(V('1.2.3.4'), V('1_2-3+4'))
    PlatformTest.assertLess(V('1.2spam'), V('1.2dev'))
    PlatformTest.assertLess(V('1.2dev'), V('1.2alpha'))
    PlatformTest.assertLess(V('1.2dev'), V('1.2a'))
    PlatformTest.assertLess(V('1.2alpha'), V('1.2beta'))
    PlatformTest.assertLess(V('1.2a'), V('1.2b'))
    PlatformTest.assertLess(V('1.2beta'), V('1.2c'))
    PlatformTest.assertLess(V('1.2b'), V('1.2c'))
    PlatformTest.assertLess(V('1.2c'), V('1.2RC'))
    PlatformTest.assertLess(V('1.2c'), V('1.2rc'))
    PlatformTest.assertLess(V('1.2RC'), V('1.2.0'))
    PlatformTest.assertLess(V('1.2rc'), V('1.2.0'))
    PlatformTest.assertLess(V('1.2.0'), V('1.2pl'))
    PlatformTest.assertLess(V('1.2.0'), V('1.2p'))
    PlatformTest.assertLess(V('1.5.1'), V('1.5.2b2'))
    PlatformTest.assertLess(V('3.10a'), V('161'))
    PlatformTest.assertEqual(V('8.02'), V('8.02'))
    PlatformTest.assertLess(V('3.4j'), V('1996.07.12'))
    PlatformTest.assertLess(V('3.1.1.6'), V('3.2.pl0'))
    PlatformTest.assertLess(V('2g6'), V('11g'))
    PlatformTest.assertLess(V('0.9'), V('2.2'))
    PlatformTest.assertLess(V('1.2'), V('1.2.1'))
    PlatformTest.assertLess(V('1.1'), V('1.2.2'))
    PlatformTest.assertLess(V('1.1'), V('1.2'))
    PlatformTest.assertLess(V('1.2.1'), V('1.2.2'))
    PlatformTest.assertLess(V('1.2'), V('1.2.2'))
    PlatformTest.assertLess(V('0.4'), V('0.4.0'))
    PlatformTest.assertLess(V('1.13++'), V('5.5.kw'))
    PlatformTest.assertLess(V('0.960923'), V('2.2beta29'))

PlatformTest = test_platform.PlatformTest()
test__comparable_version()
