
import unittest

class TestingError(unittest.TestCase):
    def test_negative_one(self):
        with self.assertRaisesRegex(AssertionError, "xxxxx"):
            self.assertEqual(1, 2)
