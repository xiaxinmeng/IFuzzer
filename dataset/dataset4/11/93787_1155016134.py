import unittest

class A:
    __var = 2

class TestMangledNamesUsage(unittest.TestCase):
    def test(self):
        a = A().__var

unittest.main()