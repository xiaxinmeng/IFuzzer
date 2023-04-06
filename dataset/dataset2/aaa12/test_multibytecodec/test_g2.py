from test import support
from test.support import os_helper
from test.support.os_helper import TESTFN
import unittest, io, codecs, sys
import _multibytecodec
import test_multibytecodec

def test_g2():
    iso2022jp2 = b'\x1b(B:hu4:unit\x1b.A\x1bNi de famille'
    uni = ':hu4:unité de famille'
    Test_ISO2022.assertEqual(iso2022jp2.decode('iso2022-jp-2'), uni)

Test_ISO2022 = test_multibytecodec.Test_ISO2022()
test_g2()
