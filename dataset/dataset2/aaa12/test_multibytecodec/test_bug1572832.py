from test import support
from test.support import os_helper
from test.support.os_helper import TESTFN
import unittest, io, codecs, sys
import _multibytecodec
import test_multibytecodec

def test_bug1572832():
    for x in range(65536, 1114112):
        chr(x).encode('iso_2022_jp', 'ignore')

Test_ISO2022 = test_multibytecodec.Test_ISO2022()
test_bug1572832()
