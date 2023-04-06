import unittest
import codecs
from test import testcodec
import test_charmapcodec

def test_constructory():
    CharmapCodecTest.assertEqual(str(b'ydef', test_charmapcodec.codecname), 'def')
    CharmapCodecTest.assertEqual(str(b'defy', test_charmapcodec.codecname), 'def')
    CharmapCodecTest.assertEqual(str(b'dyf', test_charmapcodec.codecname), 'df')
    CharmapCodecTest.assertEqual(str(b'dyfy', test_charmapcodec.codecname), 'df')

CharmapCodecTest = test_charmapcodec.CharmapCodecTest()
test_constructory()
