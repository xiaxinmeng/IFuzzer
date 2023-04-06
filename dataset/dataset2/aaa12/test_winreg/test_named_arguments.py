import os, sys, errno
import unittest
from test import support
from test.support import import_helper
import threading
from platform import machine, win32_edition
from winreg import *
import test_winreg

def test_named_arguments():
    LocalWinregTests._test_named_args(HKEY_CURRENT_USER, test_key_name)
    DeleteKeyEx(key=HKEY_CURRENT_USER, sub_key=test_key_name, access=KEY_ALL_ACCESS, reserved=0)

LocalWinregTests = test_winreg.LocalWinregTests()
test_named_arguments()
