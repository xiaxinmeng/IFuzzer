import unittest
import xdrlib
import test_xdrlib

def test_uhyper():
    ConversionErrorTest.assertRaisesConversion(ConversionErrorTest.packer.pack_uhyper, 'string')

ConversionErrorTest = test_xdrlib.ConversionErrorTest()
ConversionErrorTest.setUp()
test_uhyper()
