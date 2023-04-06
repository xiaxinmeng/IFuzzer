import secrets
import unittest
import string
import test_secrets

def test_randbelow():
    for i in range(2, 10):
        Random_Tests.assertIn(secrets.randbelow(i), range(i))
    Random_Tests.assertRaises(ValueError, secrets.randbelow, 0)
    Random_Tests.assertRaises(ValueError, secrets.randbelow, -1)

Random_Tests = test_secrets.Random_Tests()
test_randbelow()
