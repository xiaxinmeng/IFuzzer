import unittest
import codecs
from test import testcodec
import test_charmapcodec

def test_encodex():
    CharmapCodecTest.assertEqual('abc'.encode(test_charmapcodec.codecname), b'abc')
    CharmapCodecTest.assertEqual('xdef'.encode(test_charmapcodec.codecname), b'abcdef')
    CharmapCodecTest.assertEqual('defx'.encode(test_charmapcodec.codecname), b'defabc')
    CharmapCodecTest.assertEqual('dxf'.encode(test_charmapcodec.codecname), b'dabcf')
    CharmapCodecTest.assertEqual('dxfx'.encode(test_charmapcodec.codecname), b'dabcfabc')

CharmapCodecTest = test_charmapcodec.CharmapCodecTest()
test_encodex()
