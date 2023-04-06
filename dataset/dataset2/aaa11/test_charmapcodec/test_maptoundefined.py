import unittest
import codecs
from test import testcodec
import test_charmapcodec

def test_maptoundefined():
    CharmapCodecTest.assertRaises(UnicodeError, str, b'abc\x01', test_charmapcodec.codecname)

CharmapCodecTest = test_charmapcodec.CharmapCodecTest()
test_maptoundefined()
