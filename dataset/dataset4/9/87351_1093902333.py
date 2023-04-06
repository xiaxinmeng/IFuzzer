class TestAudioop(unittest.TestCase):
         pass

def test_invalid_adpcm_state():
         TestAudioop.assertRaises(TypeError, audioop.lin2adpcm, b'\x00', 1, 555)
         TestAudioop.assertRaises(test_invalid_adpcm_state(), audioop.adpcm2lin, b'\x00', 1, (0, (- 1)))

TestAudioop = TestAudioop()
test_invalid_adpcm_state()