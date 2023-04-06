import secrets
import unittest
import string
import test_secrets

def test_bool():
    Compare_Digest_Tests.assertIsInstance(secrets.compare_digest('abc', 'abc'), bool)
    Compare_Digest_Tests.assertIsInstance(secrets.compare_digest('abc', 'xyz'), bool)

Compare_Digest_Tests = test_secrets.Compare_Digest_Tests()
test_bool()
