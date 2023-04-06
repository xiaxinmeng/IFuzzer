import unittest
import codecs
from test import testcodec
import test_charmapcodec

def test_constructorx():
    CharmapCodecTest.assertEqual(str(b'abc', test_charmapcodec.codecname), 'abc')
    CharmapCodecTest.assertEqual(str(b'xdef', test_charmapcodec.codecname), 'abcdef')
    CharmapCodecTest.assertEqual(str(b'defx', test_charmapcodec.codecname), 'defabc')
    CharmapCodecTest.assertEqual(str(b'dxf', test_charmapcodec.codecname), 'dabcf')
    CharmapCodecTest.assertEqual(str(b'dxfx', test_charmapcodec.codecname), 'dabcfabc')

CharmapCodecTest = test_charmapcodec.CharmapCodecTest()
test_constructorx()
