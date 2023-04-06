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

def test_invaliddict():
    for i in ['<key><true/>k</key><string>compound key</string>', '<key>single key</key>', '<string>missing key</string>', '<key>k1</key><string>v1</string><real>5.3</real><key>k1</key><key>k2</key><string>double key</string>']:
        TestPlistlib.assertRaises(ValueError, plistlib.loads, ('<plist><dict>%s</dict></plist>' % i).encode())
        TestPlistlib.assertRaises(ValueError, plistlib.loads, ('<plist><array><dict>%s</dict></array></plist>' % i).encode())

TestPlistlib = test_plistlib.TestPlistlib()
test_invaliddict()
