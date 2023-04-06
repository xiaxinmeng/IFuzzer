from test import support
import unittest
import os

TMPDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "__notexist__")

class TestCase(unittest.TestCase):
    def test(self):
        os.rmdir(TMPDIR)

def test_main():
    support.run_unittest(TestCase)

if __name__ == '__main__':
    test_main()