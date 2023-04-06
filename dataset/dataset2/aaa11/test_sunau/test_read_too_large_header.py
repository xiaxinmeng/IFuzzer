import unittest
from test import audiotests
from audioop import byteswap
import io
import struct
import sys
import sunau
import test_sunau

def test_read_too_large_header():
    b = struct.pack('>LLLLLL', sunau.AUDIO_FILE_MAGIC, 124, 0, sunau.AUDIO_FILE_ENCODING_LINEAR_8, 11025, 1)
    b += b'\x00' * 100
    with SunauLowLevelTest.assertRaisesRegex(sunau.Error, 'header size ridiculously large'):
        sunau.open(io.BytesIO(b))

SunauLowLevelTest = test_sunau.SunauLowLevelTest()
test_read_too_large_header()
