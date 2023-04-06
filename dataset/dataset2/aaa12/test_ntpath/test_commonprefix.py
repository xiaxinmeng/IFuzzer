import ntpath
import os
import sys
import unittest
import warnings
from test.support import os_helper
from test.support import TestFailed
from test.support.os_helper import FakePath
from test import test_genericpath
from tempfile import TemporaryFile

import ctypes
import test_ntpath

def test_commonprefix():
    test_ntpath.tester('ntpath.commonprefix(["/home/swenson/spam", "/home/swen/spam"])', '/home/swen')
    test_ntpath.tester('ntpath.commonprefix(["\\home\\swen\\spam", "\\home\\swen\\eggs"])', '\\home\\swen\\')
    test_ntpath.tester('ntpath.commonprefix(["/home/swen/spam", "/home/swen/spam"])', '/home/swen/spam')

TestNtpath = test_ntpath.TestNtpath()
test_commonprefix()
