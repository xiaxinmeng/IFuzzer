import secrets
import unittest
import string
import test_secrets

def test_choice():
    items = [1, 2, 4, 8, 16, 32, 64]
    for i in range(10):
        Random_Tests.assertTrue(secrets.choice(items) in items)

Random_Tests = test_secrets.Random_Tests()
test_choice()
