import secrets
import unittest
import string
import test_secrets

def test_equal():
    for s in ('a', 'bcd', 'xyz123'):
        a = s * 100
        b = s * 100
        Compare_Digest_Tests.assertTrue(secrets.compare_digest(a, b))
        Compare_Digest_Tests.assertTrue(secrets.compare_digest(a.encode('utf-8'), b.encode('utf-8')))

Compare_Digest_Tests = test_secrets.Compare_Digest_Tests()
test_equal()
