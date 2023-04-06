import unittest

def f():
    raise TypeError

class TestAudioop(unittest.TestCase):
    def test_invalid_adpcm_state(self):
        self.assertRaises(TypeError, f) 
        self.test_invalid_adpcm_state()