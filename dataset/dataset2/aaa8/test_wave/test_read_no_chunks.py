import unittest
from test import audiotests
from test import support
from audioop import byteswap
import io
import struct
import sys
import wave
import test_wave

def test_read_no_chunks():
    b = b'SPAM'
    with WaveLowLevelTest.assertRaises(EOFError):
        wave.open(io.BytesIO(b))

WaveLowLevelTest = test_wave.WaveLowLevelTest()
test_read_no_chunks()
