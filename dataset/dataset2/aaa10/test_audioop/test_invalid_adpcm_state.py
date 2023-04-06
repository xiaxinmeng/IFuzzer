import audioop
import sys
import unittest
import test_audioop

def test_invalid_adpcm_state():
    TestAudioop.assertRaises(TypeError, audioop.adpcm2lin, b'\x00', 1, 555)
    TestAudioop.assertRaises(TypeError, audioop.lin2adpcm, b'\x00', 1, 555)
    TestAudioop.assertRaises(ValueError, audioop.adpcm2lin, b'\x00', 1, (0, -1))
    TestAudioop.assertRaises(ValueError, audioop.adpcm2lin, b'\x00', 1, (0, 89))
    TestAudioop.assertRaises(ValueError, audioop.lin2adpcm, b'\x00', 1, (0, -1))
    TestAudioop.assertRaises(ValueError, audioop.lin2adpcm, b'\x00', 1, (0, 89))
    TestAudioop.assertRaises(ValueError, audioop.adpcm2lin, b'\x00', 1, (-32769, 0))
    TestAudioop.assertRaises(ValueError, audioop.adpcm2lin, b'\x00', 1, (32768, 0))
    TestAudioop.assertRaises(ValueError, audioop.lin2adpcm, b'\x00', 1, (-32769, 0))
    TestAudioop.assertRaises(ValueError, audioop.lin2adpcm, b'\x00', 1, (32768, 0))

TestAudioop = test_audioop.TestAudioop()
test_invalid_adpcm_state()
