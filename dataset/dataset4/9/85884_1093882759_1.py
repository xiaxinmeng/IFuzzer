import unittest
import sys

class Tests(unittest.TestCase):
    def test_bug(self):
        print("len(sys.modules):", len(sys.modules))

if __name__ == "__main__":
    unittest.main()