import unittest


class TestResourceWarning(unittest.TestCase):
    def test_it(self):
        self.assertIn("TestResourceWarning", open(__file__).read())