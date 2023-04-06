import unittest
from test import support
import sys

class Tests(unittest.TestCase):
    def test_bug(self):
        modules = sorted(sys.modules)
        print("sys.modules:")
        print("")
        import pprint
        pprint.pprint(modules)
        print("")
        print("len(sys.modules):", len(modules))

def test_main():
    support.run_unittest(Tests)

if __name__ == "__main__":
    test_main()