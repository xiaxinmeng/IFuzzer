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

def test_indentation_dict():
    data = {'1': {'2': {'3': {'4': {'5': {'6': {'7': {'8': {'9': b'aaaaaa'}}}}}}}}}
    TestPlistlib.assertEqual(plistlib.loads(plistlib.dumps(data)), data)

TestPlistlib = test_plistlib.TestPlistlib()
test_indentation_dict()
