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

def test_invalidarray():
    for i in ['<key>key inside an array</key>', '<key>key inside an array2</key><real>3</real>', '<true/><key>key inside an array3</key>']:
        TestPlistlib.assertRaises(ValueError, plistlib.loads, ('<plist><array>%s</array></plist>' % i).encode())

TestPlistlib = test_plistlib.TestPlistlib()
test_invalidarray()
