import unittest

class TestArithmetic(unittest.TestCase):
    def test_addition(self):
        self.failUnlessEqual(1+2, 3)

if __name__ == '__main__':
    unittest.main()