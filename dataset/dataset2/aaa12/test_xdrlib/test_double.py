import unittest
import xdrlib
import test_xdrlib

def test_double():
    ConversionErrorTest.assertRaisesConversion(ConversionErrorTest.packer.pack_double, 'string')

ConversionErrorTest = test_xdrlib.ConversionErrorTest()
ConversionErrorTest.setUp()
test_double()
