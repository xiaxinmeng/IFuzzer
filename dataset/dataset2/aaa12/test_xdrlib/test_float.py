import unittest
import xdrlib
import test_xdrlib

def test_float():
    ConversionErrorTest.assertRaisesConversion(ConversionErrorTest.packer.pack_float, 'string')

ConversionErrorTest = test_xdrlib.ConversionErrorTest()
ConversionErrorTest.setUp()
test_float()
