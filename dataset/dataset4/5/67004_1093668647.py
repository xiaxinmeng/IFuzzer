import unittest

class TestStringMethods(unittest.TestCase):

    @unittest.expectedFailure
    def test_upper(self):
        self.assertEqual(2, 2)

    def test_lower(self):
        return

if __name__ == '__main__':
    unittest.main()