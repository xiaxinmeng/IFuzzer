import unittest
from test import audiotests
from audioop import byteswap
import io
import struct
import sys
import sunau
import test_sunau

def test_read_too_small_header():
    b = struct.pack('>LLLLL', sunau.AUDIO_FILE_MAGIC, 20, 0, sunau.AUDIO_FILE_ENCODING_LINEAR_8, 11025)
    with SunauLowLevelTest.assertRaisesRegex(sunau.Error, 'header size too small'):
        sunau.open(io.BytesIO(b))

SunauLowLevelTest = test_sunau.SunauLowLevelTest()
test_read_too_small_header()
