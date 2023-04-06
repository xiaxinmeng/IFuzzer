import copy
import operator
import pickle
import struct
import unittest
import plistlib
import os
import datetime
import codecs
import binascii
import collections
from test import support
from test.support import os_helper
from io import BytesIO
from plistlib import UID
import test_plistlib

def test_load_invalid_file():
    with TestPlistlib.assertRaises(plistlib.InvalidFileException):
        plistlib.loads(b'these are not plist file contents')

TestPlistlib = test_plistlib.TestPlistlib()
test_load_invalid_file()
