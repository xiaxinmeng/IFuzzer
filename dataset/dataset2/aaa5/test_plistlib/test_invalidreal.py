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

def test_invalidreal():
    TestPlistlib.assertRaises(ValueError, plistlib.loads, b'<plist><integer>not real</integer></plist>')

TestPlistlib = test_plistlib.TestPlistlib()
test_invalidreal()
