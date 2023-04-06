import unittest
from test import support
from test.support import os_helper
import os
import platform
import sys
from os import path
import test_startfile

def test_nonexisting():
    TestCase.assertRaises(OSError, startfile, 'nonexisting.vbs')

TestCase = test_startfile.TestCase()
test_nonexisting()
