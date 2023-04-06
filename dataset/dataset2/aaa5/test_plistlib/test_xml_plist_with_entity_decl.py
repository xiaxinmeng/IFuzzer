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

def test_xml_plist_with_entity_decl():
    with TestPlistlib.assertRaisesRegex(plistlib.InvalidFileException, 'XML entity declarations are not supported'):
        plistlib.loads(test_plistlib.XML_PLIST_WITH_ENTITY, fmt=plistlib.FMT_XML)

TestPlistlib = test_plistlib.TestPlistlib()
test_xml_plist_with_entity_decl()
