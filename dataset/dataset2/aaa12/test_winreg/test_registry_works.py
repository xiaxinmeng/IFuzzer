import os, sys, errno
import unittest
from test import support
from test.support import import_helper
import threading
from platform import machine, win32_edition
from winreg import *
import test_winreg

def test_registry_works():
    LocalWinregTests._test_all(HKEY_CURRENT_USER)
    LocalWinregTests._test_all(HKEY_CURRENT_USER, '日本-subkey')

LocalWinregTests = test_winreg.LocalWinregTests()
test_registry_works()
