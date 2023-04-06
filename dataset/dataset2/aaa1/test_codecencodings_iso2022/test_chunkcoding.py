from test import multibytecodec_support
import unittest
import test_codecencodings_iso2022

@unittest.skip('iso2022_kr.txt cannot be used to test "chunk coding"')
def test_chunkcoding():
    pass

Test_ISO2022_KR = test_codecencodings_iso2022.Test_ISO2022_KR()
test_chunkcoding()
