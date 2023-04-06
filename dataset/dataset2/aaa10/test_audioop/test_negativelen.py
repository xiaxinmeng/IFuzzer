import audioop
import sys
import unittest
import test_audioop

def test_negativelen():
    TestAudioop.assertRaises(audioop.error, audioop.findmax, bytes(range(256)), -2392392)

TestAudioop = test_audioop.TestAudioop()
test_negativelen()
