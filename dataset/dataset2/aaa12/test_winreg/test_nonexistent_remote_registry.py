import os, sys, errno
import unittest
from test import support
from test.support import import_helper
import threading
from platform import machine, win32_edition
from winreg import *
import test_winreg

def test_nonexistent_remote_registry():
    connect = lambda : ConnectRegistry('abcdefghijkl', HKEY_CURRENT_USER)
    LocalWinregTests.assertRaises(OSError, connect)

LocalWinregTests = test_winreg.LocalWinregTests()
test_nonexistent_remote_registry()
