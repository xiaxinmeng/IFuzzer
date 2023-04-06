import faulthandler
from test.support import import_helper
import unittest
import test_xxtestfuzz


_xxtestfuzz = import_helper.import_module('_xxtestfuzz')
def test_sample_input_smoke_test():
    """This is only a regression test: Check that it doesn't crash."""
    _xxtestfuzz.run(b'')
    _xxtestfuzz.run(b'\x00')
    _xxtestfuzz.run(b'{')
    _xxtestfuzz.run(b' ')
    _xxtestfuzz.run(b'x')
    _xxtestfuzz.run(b'1')
    _xxtestfuzz.run(b'AAAAAAA')
    _xxtestfuzz.run(b'AAAAAA\x00')

faulthandler.enable()
TestFuzzer = test_xxtestfuzz.TestFuzzer()
test_sample_input_smoke_test()
