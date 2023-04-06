import unittest
from test import audiotests
from audioop import byteswap
import io
import struct
import sys
import sunau
import test_sunau

def test_read_bad_magic_number():
    b = b'SPA'
    with SunauLowLevelTest.assertRaises(EOFError):
        sunau.open(io.BytesIO(b))
    b = b'SPAM'
    with SunauLowLevelTest.assertRaisesRegex(sunau.Error, 'bad magic number'):
        sunau.open(io.BytesIO(b))

SunauLowLevelTest = test_sunau.SunauLowLevelTest()
test_read_bad_magic_number()
