import unittest
class Tests(unittest.TestCase):
    def test_equal_to_five_decimal_places(self):
        """Check assertAlmostEqual using decimal places"""
        self.assertAlmostEqual(0.123456789, 0.123456, 5)
if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity = 2)
    unittest.main(testRunner=runner)