import unittest
import xdrlib
import test_xdrlib

def test_pack_uint():
    ConversionErrorTest.assertRaisesConversion(ConversionErrorTest.packer.pack_uint, 'string')

ConversionErrorTest = test_xdrlib.ConversionErrorTest()
ConversionErrorTest.setUp()
test_pack_uint()
