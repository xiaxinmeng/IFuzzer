import unittest

class T(unittest.TestCase):
    def test_f(self): raise TypeError()

unittest.main()