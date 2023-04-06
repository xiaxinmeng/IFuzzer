import sys
import unittest
import crypt
import test_crypt

def test_methods():
    CryptTestCase.assertTrue(len(crypt.methods) >= 1)
    if sys.platform.startswith('openbsd'):
        CryptTestCase.assertEqual(crypt.methods, [crypt.METHOD_BLOWFISH])
    else:
        CryptTestCase.assertEqual(crypt.methods[-1], crypt.METHOD_CRYPT)

CryptTestCase = test_crypt.CryptTestCase()
test_methods()
