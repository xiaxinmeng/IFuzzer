import unittest
from test import support
from test.support import import_helper
import binascii
import copy
import pickle
import random
import sys
from test.support import bigmemtest, _1G, _4G
import random
import test_zlib

def test_badlevel():
    ExceptionTestCase.assertRaises(test_zlib.zlib.error, test_zlib.zlib.compress, b'ERROR', 10)

ExceptionTestCase = test_zlib.ExceptionTestCase()
test_badlevel()
