import functools
import time
import unittest
from test import support
from test.support import import_helper
import test_winsound

def test_asterisk():
    safe_MessageBeep(winsound.MB_ICONASTERISK)

MessageBeepTest = test_winsound.MessageBeepTest()
test_asterisk()
