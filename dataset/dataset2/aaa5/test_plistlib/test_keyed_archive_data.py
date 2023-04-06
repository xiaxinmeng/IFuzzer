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

def test_keyed_archive_data():
    data = {'$version': 100000, '$objects': ['$null', {'pytype': 1, '$class': UID(2), 'NS.string': 'KeyArchive UID Test'}, {'$classname': 'OC_BuiltinPythonUnicode', '$classes': ['OC_BuiltinPythonUnicode', 'OC_PythonUnicode', 'NSString', 'NSObject'], '$classhints': ['OC_PythonString', 'NSString']}], '$archiver': 'NSKeyedArchiver', '$top': {'root': UID(1)}}
    TestKeyedArchive.assertEqual(plistlib.loads(test_plistlib.TESTDATA['KEYED_ARCHIVE']), data)

TestKeyedArchive = test_plistlib.TestKeyedArchive()
test_keyed_archive_data()
