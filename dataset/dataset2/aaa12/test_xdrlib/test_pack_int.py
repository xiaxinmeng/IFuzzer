import unittest
import xdrlib
import test_xdrlib

def test_pack_int():
    ConversionErrorTest.assertRaisesConversion(ConversionErrorTest.packer.pack_int, 'string')

ConversionErrorTest = test_xdrlib.ConversionErrorTest()
ConversionErrorTest.setUp()
test_pack_int()
