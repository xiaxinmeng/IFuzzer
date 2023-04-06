import unittest
from test import audiotests
from test import support
from audioop import byteswap
import io
import struct
import sys
import wave
import test_wave

def test__all__():
    support.check__all__(MiscTestCase, wave, not_exported={'WAVE_FORMAT_PCM'})

MiscTestCase = test_wave.MiscTestCase()
test__all__()
