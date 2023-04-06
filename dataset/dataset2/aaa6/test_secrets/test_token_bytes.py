import secrets
import unittest
import string
import test_secrets

def test_token_bytes():
    for n in (1, 8, 17, 100):
        with Token_Tests.subTest(n=n):
            Token_Tests.assertIsInstance(secrets.token_bytes(n), bytes)
            Token_Tests.assertEqual(len(secrets.token_bytes(n)), n)

Token_Tests = test_secrets.Token_Tests()
test_token_bytes()
