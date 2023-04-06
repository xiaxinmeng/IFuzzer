import secrets
import unittest
import string
import test_secrets

def test_unequal():
    Compare_Digest_Tests.assertFalse(secrets.compare_digest('abc', 'abcd'))
    Compare_Digest_Tests.assertFalse(secrets.compare_digest(b'abc', b'abcd'))
    for s in ('x', 'mn', 'a1b2c3'):
        a = s * 100 + 'q'
        b = s * 100 + 'k'
        Compare_Digest_Tests.assertFalse(secrets.compare_digest(a, b))
        Compare_Digest_Tests.assertFalse(secrets.compare_digest(a.encode('utf-8'), b.encode('utf-8')))

Compare_Digest_Tests = test_secrets.Compare_Digest_Tests()
test_unequal()
