import os, sys, errno
import unittest
from test import support
from test.support import import_helper
import threading
from platform import machine, win32_edition
from winreg import *
import test_winreg

@unittest.skipIf(win32_edition() in ('WindowsCoreHeadless', 'IoTEdgeOS'), 'APIs not available on WindowsCoreHeadless')
def test_reflection_functions():
    with OpenKey(HKEY_LOCAL_MACHINE, 'Software') as key:
        Win64WinregTests.assertTrue(QueryReflectionKey(key))
        Win64WinregTests.assertIsNone(EnableReflectionKey(key))
        Win64WinregTests.assertIsNone(DisableReflectionKey(key))
        Win64WinregTests.assertTrue(QueryReflectionKey(key))

Win64WinregTests = test_winreg.Win64WinregTests()
test_reflection_functions()
