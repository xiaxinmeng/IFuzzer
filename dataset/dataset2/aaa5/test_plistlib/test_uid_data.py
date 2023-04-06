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

def test_uid_data():
    uid = UID(1)
    TestPlistlib.assertEqual(uid.data, 1)

TestPlistlib = test_plistlib.TestPlistlib()
test_uid_data()
