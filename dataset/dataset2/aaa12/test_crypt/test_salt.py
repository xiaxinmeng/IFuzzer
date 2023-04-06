import sys
import unittest
import crypt
import test_crypt

def test_salt():
    CryptTestCase.assertEqual(len(crypt._saltchars), 64)
    for method in crypt.methods:
        salt = crypt.mksalt(method)
        CryptTestCase.assertIn(len(salt) - method.salt_chars, {0, 1, 3, 4, 6, 7})
        if method.ident:
            CryptTestCase.assertIn(method.ident, salt[:len(salt) - method.salt_chars])

CryptTestCase = test_crypt.CryptTestCase()
test_salt()
